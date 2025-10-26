from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, crud, utils, image_generator
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/countries")
def get_countries(region: str = None, currency: str = None, sort: str = None, db: Session = Depends(get_db)):
    return crud.get_countries(db, region, currency, sort)

@app.get("/countries/{name}")
def get_country(name: str, db: Session = Depends(get_db)):
    country = crud.get_country_by_name(db, name)
    if not country:
        raise HTTPException(status_code=404, detail={"error": "Country not found"})
    return country

@app.post("/countries/refresh")
def refresh_countries(db: Session = Depends(get_db)):
    try:
        countries = utils.fetch_countries()
        rates = utils.fetch_exchange_rates()
    except Exception as e:
        raise HTTPException(status_code=503, detail={"error": "External data source unavailable"})

    for c in countries:
        currency = c.get("currencies", [{}])[0] if c.get("currencies") else {}
        code = currency.get("code")
        rate = rates.get(code)
        gdp = utils.compute_gdp(c.get("population", 0), rate)

        crud.upsert_country(db, {
            "name": c.get("name"),
            "capital": c.get("capital"),
            "region": c.get("region"),
            "population": c.get("population", 0),
            "currency_code": code,
            "exchange_rate": rate,
            "estimated_gdp": gdp,
            "flag_url": c.get("flag"),
        })

    all_countries = crud.get_countries(db)
    top5 = sorted(all_countries, key=lambda x: x.estimated_gdp or 0, reverse=True)[:5]
    image_generator.generate_summary_image(len(all_countries), top5)

    return {"message": "Countries refreshed successfully", "total": len(all_countries)}

@app.get("/countries/image")
def get_summary_image():
    path = "cache/summary.png"
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail={"error": "Summary image not found"})
    from fastapi.responses import FileResponse
    return FileResponse(path)

@app.get("/status")
def get_status(db: Session = Depends(get_db)):
    total = len(crud.get_countries(db))
    return {"total_countries": total, "last_refreshed_at": "To be added dynamically later"}
