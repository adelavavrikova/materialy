# Bonus 1 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci zkontroluj_pin(spravny_pin), která dá uživateli
#     tři pokusy zadat PIN. Když se trefí, vrátí True, jinak False.
#     Po zavolání vypiš "Odemčeno." nebo "Karta zablokována.".


def check_pin(spravny_pin):
    pokusy = 0
    while pokusy < 3:
        zadany = input("Zadej PIN:")
        pokusy = pokusy + 1
        if zadany == spravny_pin:
         return True
        print("Špatný pin")
    return False
if check_pin("1234"):
    print("Odemčeno.")
else:
    print("Karta zablokována.")