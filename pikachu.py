import requests
 
 
def pika():
    lenkeTilApi = "https://pokeapi.co/api/v2/pokemon/pikachu"
 
    hentetApi = requests.get(lenkeTilApi)
 
    print(f"her er statuskoden for henting: "+str(hentetApi.status_code))
    if hentetApi.status_code != 200:
        print("ALT IKKE OK")

 
    innholdetItekst = hentetApi.json()
 
    høyde = innholdetItekst["height"]
    vekt = innholdetItekst["weight"]

    return høyde , vekt
