# Bonus 3 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Bum-Bác pro jedno číslo.
#     Zeptej se na číslo a vypiš:
#       - "BumBác", když je dělitelné třemi i pěti zároveň,
#       - "Bum", když je dělitelné jen třemi,
#       - "Bác", když je dělitelné jen pěti,
#       - jinak samotné číslo.

cislo = int(input("rekni cislo"))

if cislo % 15 == 0:
    print("BumBác")
elif cislo % 3 == 0:
    print("Bum")
elif cislo % 5 == 0:
    print("Bác")
else:
    print(cislo)