import requests
import os
from dotenv import load_dotenv


def weather():
    load_dotenv()
    lat = 60
    lon = 10 
    API = os.getenv("API")

    lenkeTilApi = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}&units=metric"
 
    hentetApi = requests.get(lenkeTilApi)
 
    print(f"her er statuskoden for henting: "+str(hentetApi.status_code))
    if hentetApi.status_code != 200:
        print("ALT IKKE OK")

    innholdetItekst = hentetApi.json()

    temperatur = innholdetItekst["main"]["temp"]

    return innholdetItekst