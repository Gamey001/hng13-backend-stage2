import requests, random

COUNTRY_API = "https://restcountries.com/v2/all?fields=name,capital,region,population,flag,currencies"
EXCHANGE_API = "https://open.er-api.com/v6/latest/USD"

def fetch_countries():
    r = requests.get(COUNTRY_API, timeout=10)
    r.raise_for_status()
    return r.json()

def fetch_exchange_rates():
    r = requests.get(EXCHANGE_API, timeout=10)
    r.raise_for_status()
    return r.json().get("rates", {})

def compute_gdp(population, exchange_rate):
    if not exchange_rate or exchange_rate == 0:
        return 0
    multiplier = random.randint(1000, 2000)
    return (population * multiplier) / exchange_rate
