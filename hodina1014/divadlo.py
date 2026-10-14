pocet = int(input("Zadej počet lidí: "))
cena_vstupenka = 500

# default hodnoty pro případ, že není sleva
typ_slevy = "Beze slevy"
cena_celkova = cena_vstupenka * pocet

if pocet >= 4:
    cena_celkova = cena_vstupenka * pocet * 0.75
    typ_slevy = "skupinová sleva"
else:
    # zde řeším individuální ceny (včetně slev)
    vek = float(input("Zadej věk: "))
    if vek >= 65:
        # senior
        cena_celkova = cena_vstupenka * pocet * 0.8
        typ_slevy = "senioři"
    elif vek < 26:
            # toto by mohl být student
            student = input("Jste student? (ano/ne): ")
            if student == "ano":
                cena_celkova = cena_vstupenka * pocet * 0.7
                typ_slevy = "studentská sleva"
print("Cena 1 osoba", cena_celkova / pocet)
print("Cena celkem:", cena_celkova)
print(typ_slevy)