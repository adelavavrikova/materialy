#dostudovat doma, nerozumím, ale musím si definovat začátek součtu, když nechci, aby se mi věci resetovaly, musím je ukotvit mimo cyklus

soucet = 0
for i in range (0,5):
    print ("i", i)
    print ("soucet na zacatku cyklu:", soucet)
    soucet = soucet + i
    print ("soucet na konci cyklu:", soucet)
print("po cyklu:", soucet)

# co když chci, aby se mi něco opakovalo 4x v každým cyklu, je to koncept vnořeného cyklu, cyklus s emá opakovat 5x a chci aby se mi v něm
# něco 4 x opakovalo

for i in range(5):
    print(i)
    for j in range(4):
        print("Kolo:", i, "pokus:", j)
    print("konec", i)
print ("konec vsech cyklu")

#priklad, jak to funguje např. pro kalendář, šlo by to rozšířit i o měsíce, přídá se vnější cyklů

for mesic in range (1,13)
    print("mesic", mesic)
    for tyden in range(5):
        print("tyden:", tyden)
        for den in range(1, 8)
            print("Tyden", tyden, "den", den)
        print ("konec tydne", tyden)
    print("konec mesice", mesic)
print ("konec kalendare")

# procházení něčím jiným než je range, vracíme se k jménu, zvládám procházet i něco jiného než range, tady u toho prvního příkladu se to
# např. vyhláskuje, hodí se to pokud bych chtěla zadat jména a nechci velká písmena, tak se dá kontrolovat, zda jsou velká písmena

jmeno = input("Name?")

for pismeno in jmeno:
    print(pismeno)