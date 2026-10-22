# Cvičení 4 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Máš proměnnou barva se stavem semaforu ("červená", "oranžová"
#    nebo "zelená"). Vypiš, co má řidič udělat:
#    "červená" → "Stůj", "oranžová" → "Připrav se", "zelená" → "Jeď",
#    cokoli jiného → "Neznámý signál".
barva = "fialová"

if barva == "zelená":
    print("Jeď!")
    if barva == "oranžová":
        print("Připrav se")
        if barva == "červená":
            print("Stůj!")
else:
    print("Semafor je rozbitý")