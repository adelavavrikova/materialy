# sep = funkce, která je separator a dá se vložit do printu
# end = fuknce, která přidá nakonec to, co specifikuju
# input = další funkce, která vrací hodnotu
# funkce mají argumenty, které mají vstup, a mohou nám i něco vracet, např. v printu to je tak, že nic nevrací

print (1, 2, 3, sep = "–––", end = "!!!")
vek = int (input ("How old are you?"))

if vek < 0:
    print("You are not alive")
else:
    print("I am sorry you live in climate catastrophe")

# některé funkce pracují s řerězcema, je důležité vědět, zda jsou to čísla, musí se to převádět, aby to bylo ve stejných hodnotách

print (vek + 1)

# nová funkce metoda len, zkrácení pro délku, můžeme ji použít na textové hodnoty, vrací to délku řetězce (odpovědi),
# len počítá všechno, i mezery, takže Ahoj Adélo, je o znak delší, zkráka jako ve Wordu, délka řetězce je něco jiného než pozice v řetězci

jmeno = input("What is your name?")
print ("Your name is", len(jmeno), "characters long")

print(len("A") + 2) # výsledek tohohle je tři

# abs = absolutní hodnota, ignoruje to záporná čísla

print(abs(-7)) # toto je 7

# další zajímá funkce je round (zaokrouhlit), pokud chci na dvě desetinné čísla, musím přidat ndigits, přidám číslo, které chci za čárku

print(round(3.14159))
print(round(3.14159, 2))

# min , minimální hodnota, z výčtu to vybere nejnižší hodnotu (i zápornou), max to dělá obráceně

print(min(-5, 0, 5))
print(max(-5, 0, 5))

# vrací mi to hodnotu, s kterou může dále pracovat např. true /false, třeba jestli nejmenší hodnota ze všeho je menší než 100

print(min(-5, 0, 5) < 4)

# range, velmi důležitá funkce, vrací čísla od zadaného čísla, specifikujeme číslo, které dává interval 
# (když je to 5, je to jen 0, 1, 2, 3, 4), když do toho přidám len, tak mi to vrátí 5, protože ot počítá i nulu
# je to trochu divný, to spodní číslo je included, to horní číslo není, takže min by byla 0, ale max je vždy o jedno níže

print(range(5))
print(len(range(5)))

# foreloop / cyklus, něco chceme dělat několikrát, zatím jsme museli používat násobit nebo to napsat vícekrát
# i je proměna, která má v sobě hodnotu toho, čím procházíme, v té první části s tím "i" vůbec nepracujeme, v každém cyklu obsahuje to číslo
# prostě se vytiskne, v jakém cyklu se ta hodnota vyhodila
# tohle se dá ilustrovat, když člověk používá debugger, kterej vypisuje kód krok po kroku

# str je opak int, když to chci vrátit zpátky do řetězce, potřebuji tam dá str nebo oddělovat čárkou

for i in range(4):
    print("Ahoj")

for i in range(4):
    print("Ahoj", str(i))

for i in range(10):
    if (i % 2 == 0):
        print("sude", str(i))
    else:
        print("liche")


# když se špatně dávájí tab, vytiskne se mi to dvakrát, protože for je ten loop a ten je definovaný, že běží víckrát, 
# hotovo se mi nevytiskne, protože se splní podmínky a hotovo není ve foreloopu a pak se vytiskne hotovo

print("Začátek")
for i in range(10):
    print("Cislo")
    if (i % 2 == 0):
        print("sude", str(i))
    else:
        print("liche")
print("Hotovo")