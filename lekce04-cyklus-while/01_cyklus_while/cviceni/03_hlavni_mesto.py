# Cvičení 3 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se uživatele "Jaké je hlavní město Česka? " tak dlouho,
#    dokud nenapíše "Praha". Pak vypiš "Správně!".

odpoved = input ("Jaké je hlavní město ČR?")
while odpoved != "Praha":
        print("To není správně, zkus znovu")
        odpoved = input ("Jaké je hlavní město ČR?")
print("Správně!")