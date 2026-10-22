# Cvičení 5 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Pořád dokola se ptej "Napiš slovo: " a to slovo vypiš.
#    Když uživatel napíše "konec", ukonči cyklus příkazem break.
#    Použij while True.


slovo = input("Napiš slovo, když napíše KONEC, tak to skončí")

while True:
    if slovo != "END":
        print("Napsala jsi:", slovo)
        slovo = input("Napiš slovo, když napíšeš END, tak to skončí")
    print("Už nic nepiš.")
