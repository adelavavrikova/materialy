# Bonus 1 – Definice funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci obdelnik(sirka, vyska), která z hvězdiček vypíše
#     obdélník zadané velikosti. obdelnik(5, 3) vypíše tři řádky
#     po pěti hvězdičkách.


def obdelnik(sirka, vyska):
    for radek in range(vyska):
        print("*" * sirka)


obdelnik(5, 3)

obdelnik(2,2)