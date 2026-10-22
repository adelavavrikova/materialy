pismeno = "hello"

for i in pismeno:
    print(pismeno)

# pronmena za for proste urcuje, ze se to rozlozi na jednotlive elementy (je to jedno jeslti jsou to pismena nebo cisla)

#for cislo in veta: #z nejakyho duvodu mi to nechce uznat vetu
    #print(cislo)

# kdyz chci aby se me to ptalo dokola na to heslo, potrebuju pouzit while loop, dokud neplati nejaka podmina

#heslo = input("Zadej heslo")
#while heslo != "pyladies":
    #print("Neprihlasena")
    #heslo = input("Zadej heslo")
#print("Vítej")

# tu promenou musim znova vypsat, protoze ji pouzivat v jinym levelu, jakoby uvnitr podminky
# vysledek inputu si pamatuje to co mi to vrátí ne tu funkci (pamatuju si to jen ten vysledek)
# nekdy se chceme z toho kodu pryc, treba chceme jeste nejakou jinou podminku, abychom ukoncili while cyklus

from random import randrange

# hazis kostkou, dokud nehodis šestku, tak musíš házet pořád dál, není tam definovaný input, takže ta hra se hraje sama

hod = randrange(1,7)
while hod != 6:
    print("Padlo", hod, "házíme znovu")
    hod = randrange(1,7)
print("Vítězíš")    

# hteďka složitěšjí varianta, že když hodím 1, tak jsem prohrála a už nehraju
# podminka se musi vložit do toho cyklu a musí být na začátku jinak to nebude kontrolovat ten první hod

hod = randrange(1, 7)
while hod != 6:
    if hod == 1:
        print("Padla jednička, končíš.") #sem by bylo mozne napsat i padla hod končíš
        break
    print("Padlo", hod, "- házíme znovu.")
    hod = randrange(1, 7)
print("Vítězíme")

# rozsirenejsi verze s jinyma podminka

hod = randrange(1,7)
while hod < 6
    if hod == 1:
        print ("Padlo", hod, "Končíš.")
        break
    print("Padlo:", hod, "hazíme znovu")
    hod = randrange (1,7)
if hod == 1:
    print ("Prohrala si")
else:
    print("Padla,", hod, "vyhrala jsi")

# jak pouzivat break, neboli vystoupeni z cyklu, bude se me to donekocna ptat, nez reknu spatne a pak se to skonci

while True:
    odpoved = input("Jak se mas?")
    if odpoved == "spatne"
        print("To je blby cau")
        break
    print("Ahoj")
print("Jejda, ja se s tebou buudu klidne bavit")