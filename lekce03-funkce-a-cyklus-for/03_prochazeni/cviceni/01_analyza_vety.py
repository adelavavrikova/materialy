# Cvičení 1 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Analýza věty. Uživatel zadá větu. Projdi ji znak po znaku a vypiš
#    počet znaků, počet samohlásek, počet mezer a počet slov ve větě.
#    (Počet slov = počet mezer + 1.)

veta = input("Write a short sentence")

samohlasky = 0
mezery = 0

for znak in veta:
    if znak in "aeiou":
        samohlasky = samohlasky + 1
    if znak == " ":
        mezery = mezery + 1

print("Počet znaků:", len(veta))
print("Samohlásek:", samohlasky)
print("Mezer:", mezery)
print("Slov:", mezery + 1)     