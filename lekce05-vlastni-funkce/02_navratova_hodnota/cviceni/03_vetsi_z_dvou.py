# Cvičení 3 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci vetsi(a, b), která vrátí větší z obou čísel.
#    Funkci max nepoužívej.

def vetsi (a,b):
    if a > b:
        return "A"
    elif a == b:
        return "Jsou stejné"
    else:
        return "B"

print(vetsi(18,20))

def vetsi(a, b):
    if a > b:
        return a
    else:
        return b