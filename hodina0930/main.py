# **********************
# Kalkulačka spropitného
# 30.9. 2026
# **********************

print("KALKULAČKA SPROPITNÉHO")     # titulní text

celkova_cena = float(input("Zadejte celkovou cenu účtu: "))
spropitne = int(input("Zadejte procento spropitného: "))
pocet_lidi = int(input("Zadejte počet lidí: "))

# celkova_cena = celkova_cena + celkova_cena * spropitne / 100
celkova_cena += celkova_cena * spropitne / 100
print(celkova_cena)

uhrada_za_jednoho = round(celkova_cena / pocet_lidi + 0.5) # připoctu 0.5, aby zaokrouhlovalo na cela cisla smerem nahoru
print(f"Celková cena: {celkova_cena} dělená {pocet_lidi} je po zaokrouhlení {uhrada_za_jednoho}")
