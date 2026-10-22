# Cvičení 3 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Přihlášení. Správné jméno je "anna" a správné heslo je "tajne".
#    Zeptej se na jméno i heslo a vypiš "Vítej!", jen když sedí obojí.
#    Jinak vypiš "Špatné údaje.".

jmeno = "anna"
heslo = "tajne"

if jmeno == "anna" and heslo == "tajne":
    print("Vítej")
else: 
    print("Špatné údaje")


jmeno = input("Zadej uzivatelske jmeno")
heslo = input("Zadej heslo")

if jmeno == "anna" and heslo == "tajne":
    print("Vítej")
else: 
    print("Špatné údaje")