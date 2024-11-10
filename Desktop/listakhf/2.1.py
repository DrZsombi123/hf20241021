szavak = []
bekertszo = None
while bekertszo != '':
    bekertszo = input(str("Adjon meg a-val kezdődő szavakat."))
    if bekertszo == '':
        break
    if bekertszo.startswith("a"):
        szavak.append(bekertszo)
print(", ".join(szavak))
