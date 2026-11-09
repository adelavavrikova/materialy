# Cvičení 3 – Definice funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci ohodnot_znamku, která má na vstupu celé číslo a vypíše:
#    1 → "Výborně", 2 → "Chvalitebně", 3 → "Dobře",
#    cokoliv jiného → "Ještě zabereme".
#    Zavolej ji v cyklu for pro známky 1 až 5.

def ohodnot_znamku(cele_cislo):
    if cele_cislo == 1:
        print("Výborně")
    elif cele_cislo == 2:
        print("Chvalitebně")
    elif cele_cislo == 3:
        print("Dobře")
    elif cele_cislo == 4:
        print("Dostatečně")
    elif cele_cislo == 5:
        print("Nedostatečně")
    else:
        print("Díky bohu, že už Tě takhle nikdo nehodnotí.")

ohodnot_znamku(1)
ohodnot_znamku(100)

# pokud je to pro vsechny cisla, muzu si to vyvolat rangem

for znamka in range(1, 12):
    ohodnot_znamku(znamka)
