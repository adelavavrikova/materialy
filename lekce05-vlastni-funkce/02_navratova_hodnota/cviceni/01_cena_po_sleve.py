# Cvičení 1 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci cena_po_sleve(cena, sleva), která vrátí cenu
#    sníženou o slevu v procentech. cena_po_sleve(200, 25) vrátí 150.0.
#    Vypiš cenu 200 Kč se slevou 25 % a cenu 1200 Kč se slevou 10 %.


def cena_po_sleve (cena, sleva):
    print ("Cena po slevě je", cena * (sleva/100), "Kč")

cena_po_sleve (200, 25)
cena_po_sleve (1200, 10)

# blbě neumím počítat

def cena_po_sleve(cena, sleva):
    return cena - cena * sleva / 100


print("200 Kč se slevou 25 %:", cena_po_sleve(200, 25))
print("1200 Kč se slevou 10 %:", cena_po_sleve(1200, 10))