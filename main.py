#Zadanie 1

slownik = {"piekarnia": ["chleb", "pączek", "bułki"], "warzywniak": ["marchew", "seler", "rukola"]}
x = 0

# jedna linijka a zajęło mi sporo czasu i kawy by to pojąć :/

nowy_slownik = {key:  [i.capitalize() for i in value] for key,value in slownik.items()}  


for key, value in nowy_slownik.items():
    
    print()
    print("Idę do ", key.capitalize() , "i kupuję tam ", value)


for k, v in slownik.items():
    x += len(v)
    
print("W sumie kupuję ", x, "produktów.")
