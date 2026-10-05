cislo=float(input("Zadejte číslo: "))


if cislo>0:
    print("Zadané číslo je kladné.")
else:
    if cislo<0:
        print("Zadané číslo je záporné.")
        cislo = -cislo
        absolutni_hodnota = -cislo
    else:
        print("Zadané číslo je nula.")


print(f"Absolutní hodnota {cislo} je {absolutni_hodnota}")