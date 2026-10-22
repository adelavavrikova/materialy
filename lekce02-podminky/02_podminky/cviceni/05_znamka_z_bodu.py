# Cvičení 5 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na počet bodů z testu (0 až 100) a vypiš známku:
#    90 a víc → 1, 75 a víc → 2, 60 a víc → 3, 40 a víc → 4,
#    jinak → 5.

body = int(input("Kolik jsi získal bodů? "))

if body >= 90:
    print("Máš jedničku, to je fajn")
elif body >= 75:
    print("Máš dvojku, to je taky fajn")
elif body >= 60:
    print("Máš trojku, to je taky fajn, ale už míň fajn")
elif body >= 40:
    print("Máš čtyřku, což je fajn, není to pěkta")
else:
    print("Neuspěla si, ale můžeš to zkusit jindy, což je fajn")