# Bonus 2 – Vstup od uživatelky
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na částku a na počet lidí.
#     Vypiš, kolik zaplatí každý a kolik korun zbyde.

people = int(input("How many people are going to split the bill?"))
bill = int(input("How muchy is it for all?"))
print("Everyone pays", bill // people,"the dog will pay the rest –", bill % people)
