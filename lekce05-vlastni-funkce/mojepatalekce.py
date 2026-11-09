#jmeno promenne ma byt deskriptivni, aby bylo jasne, co se v ni pouziva
#pokud je za slovem zavorky, bude to funkce (jinak to jsou rezervovana klicova slova)

#nechci 10x za sebou opakovat aktualni cislo je neco, tak si vypisu cyklus, dalo by se to teoreticky napsal i while cyklusem

for cislo in range(1,11):
    print("Aktualni cislo je: ", cislo)

# pak muze prijit clovek, ktery by to chtel cele nejak menit, tak to maximum nahradim promenou a ta pak meni nekdo jiny

max_hodnota = 5

for cislo in range(1,max_hodnota):
    print("Aktualni cislo je: ", cislo)

# cele tyto dva radky muzu definovat vlastni fuknci, abych to nemusela takhle psat, ale spustit to jednim kodem
# def je zkratka pro definuj funkci, pak dam jmeno funkce a pak zavorky, kam schovam to, co se ma stat
# napsala jsem tam max_hodnota, takze to vi, ze to ma dostat hodnotu, ale ono to tu hodnotu nepouziva, protoze je tam napsan text

#def vypis_cisla_do_max_hodnoty(max_hodnota):
#    print("Funguje to!")

#vypis_cisla_do_max_hodnoty(10)
#vypis_cisla_do_max_hodnoty(100)
#vypis_cisla_do_max_hodnoty(1000)

# chci aby to byla funkce co pracuje s cislama, takze ot jdu prepsat na tu for akci

def vypis_cisla_do_max_hodnoty(max_hodnota):
    for aktualni_cislo in range(1, max_hodnota):
        print(aktualni_cislo)

vypis_cisla_do_max_hodnoty(10)
vypis_cisla_do_max_hodnoty(100)
vypis_cisla_do_max_hodnoty(1000)

# kdyz si chci oznacit ty funkci, a pridat tam vodorovnou caru

def vypis_cisla_do_max_hodnoty(max_hodnota, jmeno_volani):
    for aktualni_cislo in range(1, max_hodnota):
        print(jmeno_volani, ":", aktualni_cislo)

vypis_cisla_do_max_hodnoty(1, "Volani A")
print("–"*30)
vypis_cisla_do_max_hodnoty(5, "Volani B")
print("–"*30)
vypis_cisla_do_max_hodnoty(10, "Volani C")

# ta dlouha cara muze byt i soucast ty funkce

def vypis_cisla_do_max_hodnoty(max_hodnota, jmeno_volani):
    for aktualni_cislo in range(1, max_hodnota):
        print(jmeno_volani, ":", aktualni_cislo)
    print("–"*30)

vypis_cisla_do_max_hodnoty(1, "Volani A")
print("–"*30)
vypis_cisla_do_max_hodnoty(5, "Volani B")
print("–"*30)
vypis_cisla_do_max_hodnoty(10, "Volani C")

# kdyz to ale treba nechci za tou posledni, tak to muzu oramovat jeste podminkou if

def vypis_cisla_do_max_hodnoty(max_hodnota, jmeno_volani, ukaz_caru):
    for aktualni_cislo in range(1, max_hodnota):
        print(jmeno_volani, ":", aktualni_cislo)
    if ukaz_caru:
        print("–"*30)

vypis_cisla_do_max_hodnoty(1, "Volani A", True)
print("–"*30)
vypis_cisla_do_max_hodnoty(5, "Volani B", True)
print("–"*30)
vypis_cisla_do_max_hodnoty(10, "Volani C", False)

# tedka takovy vychozi hodnota, ja ji tam vetsinou chci a jenom kdyz si nekdo rekne, ze ji neche, tak to pouzije jinou hodnotu
#pak tu funkci mohu volat se dvema nebo se treba hodnotama
# tato vychozi vec ale musi byt posledni polozka, nebo bude i u vsech promennych chtit, aby mely prirazenou hodnotu

def vypis_cisla_do_max_hodnoty(max_hodnota, jmeno_volani, ukaz_caru=True):
    for aktualni_cislo in range(1, max_hodnota):
        print(jmeno_volani, ":", aktualni_cislo)
    if ukaz_caru:
        print("–"*30)

vypis_cisla_do_max_hodnoty(1, "Volani A")
print("–"*30)
vypis_cisla_do_max_hodnoty(5, "Volani B")
print("–"*30)
vypis_cisla_do_max_hodnoty(10, "Volani C", False)