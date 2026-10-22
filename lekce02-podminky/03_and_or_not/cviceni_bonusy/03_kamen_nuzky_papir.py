# Bonus 3 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Kámen, nůžky, papír. Zeptej se obou hráčů na tah – ať zadají
#     "kamen", "nuzky" nebo "papir". Vypiš, kdo vyhrál:
#       - "Remíza.", když mají oba stejně,
#       - jinak urči vítěze podle pravidel:
#           kámen tupí nůžky, nůžky stříhají papír, papír balí kámen.
#     Vypiš "Vyhrál hráč 1." / "Vyhrál hráč 2.".


hrac1 = input ("Say kámen or nůžky or papír")
hrac2 = input ("Say kámen or nůžky or papír")

if hrac1 == hrac2:
    print("Remíza.")
elif (hrac1 == "kamen" and hrac2 == "nuzky") or (hrac1 == "nuzky" and hrac2 == "papir") or (hrac1 == "papir" and hrac2 == "kamen"):
    print("Vyhrál hráč 1.")
else:
    print("Vyhrál hráč 2.")