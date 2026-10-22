# Cvičení 6 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Zabezpečení domu. Dům je zabezpečený, jen když jsou zavřené dveře,
#    zavřená okna a zároveň zapnutý alarm.
#    Zeptej se na všechny tři věci (ano/ne). Pomocí not (…) vypiš
#    "Pozor, dům není zabezpečený!", když zabezpečený NENÍ,
#    jinak vypiš "Zabezpečeno.".

doors = input("Are the doors closed? Y/N")
windows = input ("Are the windows closed? Y/N")
alarm = input ("Is the alarm on? Y/N")

if not doors == "Y" and windows == "Y" and alarm == "Y":
    print("Dům není zabezpečený")
else:
    print("Dům je zabezpečný")
