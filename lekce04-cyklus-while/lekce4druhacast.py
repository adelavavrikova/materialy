# magicke slovicko je break / rozseknuti a vystoupeni z cyklu
# nekdy chceme ukoncit jenom jeden beh, nez trebe cely cyklus, mam cyklus o trech bezich a chci treba prerusit jenom beh ale ne cyklus
# na to je slovicko continue, vraci me hned na zacatek cyklu k While nedojede se cely cyklus
# kdyz chci pracovat s promenou scitani, musim si dat soucet nahoru
# v tom souctu nikdo nedojde k odcitani tech zapornych cisel, protoze continue mi to vrati na zacatek a nic se neodecte

soucet = 0
while True:
    odpoved = input("Zadej cislo (nebo !konec!)")
    if odpoved == "!konec!":
        break

    cislo = int(odpoved)
    if cislo < 0:
        print("Zapona cisla ignorujme")
        continue
    soucet = soucet + cislo
    print("Zatim mam:", soucet)
print("Soucet", soucet)

# kdyz chci aby to bezelo jenom petkrat je to for cyklus

soucet = 0
for i in range (0,5):
    odpoved = input("Zadej cislo (nebo !konec!)")
    if odpoved == "!konec!":
        break

    cislo = int(odpoved)
    if cislo < 0:
        print("Zapona cisla ignorujme")
        continue
    soucet = soucet + cislo
    print("Zatim mam:", soucet)
print("Soucet", soucet)