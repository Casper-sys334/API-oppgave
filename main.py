from cat import cat
from pikachu import pika
from weather import weather

print("hva vil du skal skje")
print("1 at du får en random fakta om katter")
print("2 at du får høyde og vekten til pikachu")
print("3 at du får været i Oslo")

valg = input("velg enten 1,2,3:")

if valg == "1":
    katt = cat()
    print(katt)
elif valg == "2":
    pikachu = pika()
    print(pikachu)
elif valg == "3":
    vær = weather()
    print(vær)
else:
    print("ugyldig valg")
