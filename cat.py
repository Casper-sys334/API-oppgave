import requests
 
 
 
lenkeTilApi = "https://catfact.ninja/fact"
 
hentetApi = requests.get(lenkeTilApi)
 
print(f"her er statuskoden for henting: "+str(hentetApi.status_code))
if hentetApi.status_code != 200:
    print("ALT IKKE OK")

 
innholdetItekst = hentetApi.json()
 
print(type(innholdetItekst))
 
print(innholdetItekst)