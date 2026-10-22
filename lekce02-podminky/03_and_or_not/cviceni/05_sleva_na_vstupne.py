# Cvičení 5 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Sleva na vstupné. Slevu mají děti (do 18 let) a senioři (65 a víc).
#    Navíc mají v pondělí slevu úplně všichni.
#    Zeptej se na věk a na den a vypiš "Máš slevu." / "Plné vstupné.".

vek = int(input("Kolik ti je let?"))
den = input("Jaky je dnes den?")

if vek < 18 and vek > 65 or den == "pondělí":
    print("Gratulki, dneska máš slevu")
else:
    print("Dneska nemůžeš mít slevněný lístek, přijď v pondělí")
