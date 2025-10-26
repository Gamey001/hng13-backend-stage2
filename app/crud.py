from sqlalchemy.orm import Session
from . import models
from datetime import datetime

def get_country_by_name(db: Session, name: str):
    return db.query(models.Country).filter(models.Country.name.ilike(name)).first()

def get_countries(db: Session, region=None, currency=None, sort=None):
    query = db.query(models.Country)
    if region:
        query = query.filter(models.Country.region == region)
    if currency:
        query = query.filter(models.Country.currency_code == currency)
    if sort == "gdp_desc":
        query = query.order_by(models.Country.estimated_gdp.desc())
    return query.all()

def upsert_country(db: Session, country_data: dict):
    existing = get_country_by_name(db, country_data["name"])
    if existing:
        for key, value in country_data.items():
            setattr(existing, key, value)
        existing.last_refreshed_at = datetime.utcnow()
    else:
        db.add(models.Country(**country_data))
    db.commit()

def delete_country(db: Session, name: str):
    country = get_country_by_name(db, name)
    if country:
        db.delete(country)
        db.commit()
        return True
    return False
