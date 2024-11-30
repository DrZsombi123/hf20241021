import random
db = 0
szamlalo = 1
while szamlalo <= 20:
    random_szam = random.randint(1, 12)
    if random_szam % 3 == 0:
        print(random_szam)
        db += 1
    szamlalo += 1

print ("Összes 3-al osztható szám a 20-ból: "+ str(db))