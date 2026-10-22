# Bonus 1 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá celkovou cenu útraty a počet lidí. Vypiš, kolik
#     zaplatí každý, zaokrouhleno na dvě desetinná místa.

utrata = int(input("Celková útrata:"))
lidi = int(input("Počet lidí:"))
castka = round(utrata / lidi, 2)

print("Každý zaplatí", castka)