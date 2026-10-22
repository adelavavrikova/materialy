# Cvičení 2 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Začni s číslem 1 a v cyklu ho pořád zdvojnásobuj. Zastav se,
#    jakmile přesáhne 1000, a vypiš, kolikrát jsi ho zdvojnásobila.


cislo = 1
kolikrat = 0
while cislo <= 1000:
    cislo = cislo * 2
    kolikrat = kolikrat + 1
print("NUMBER", cislo)
print("How many times", kolikrat)