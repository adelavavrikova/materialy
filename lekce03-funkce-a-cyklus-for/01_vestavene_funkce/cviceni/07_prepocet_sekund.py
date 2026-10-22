# Cvičení 7 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá počet sekund (třeba 3661). Přepočítej ho na hodiny,
#    minuty a sekundy a vypiš je jako 1:1:1 jediným printem.


pocet = int(input ("Enter the number of seconds"))

hodiny = pocet // 3600
minuty = (pocet % 3600) // 60
sekundy = pocet % 60

print(hodiny, ":", minuty, ":", sekundy)

# místo těch dvouteček se dá za čárku napsat sep = ":"