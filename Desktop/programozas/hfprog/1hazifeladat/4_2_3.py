szam = int(input("Adj meg egy számot."))

if szam % 3 == 0 and szam % 4 == 0:
    print("A szam osztható néggyel és hárommal.")
elif szam % 3 == 0:
    print("A szam osztható hárommal.")

elif szam % 4 == 0:
    print("A szam osztható néggyel.")

else:
    print("A szám se néggyel sem hárommal nem osztható")
