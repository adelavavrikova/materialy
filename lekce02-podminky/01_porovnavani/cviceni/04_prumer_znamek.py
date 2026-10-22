# Cvičení 4 – Porovnávání
# Doplň kód pod zadání a soubor spusť (Run).

# Studentka má tři známky. Spočítej jejich průměr do proměnné prumer
#    a vypiš True/False podle toho, jestli má na vyznamenání
#    (průměr menší nebo rovný 2).
#    Zamysli se: kdyby vyšlo True, co by program mohl studentce napsat?
znamka1 = 1
znamka2 = 3
znamka3 = 2

prumer = (znamka1 + znamka2 + znamka3)/3
vysledek = prumer <= 2

print("Je pravda, že studentka ma vyznamenani,", vysledek)
