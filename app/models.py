from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    capital = Column(String)
    region = Column(String)
    population = Column(Integer, nullable=False)
    currency_code = Column(String)
    exchange_rate = Column(Float)
    estimated_gdp = Column(Float)
    flag_url = Column(String)
    last_refreshed_at = Column(DateTime, default=datetime.utcnow)
