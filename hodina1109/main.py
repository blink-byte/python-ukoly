import math

print("Test prvočísla")
cislo = int(input("Zadejte celé číslo: "))

je_prvocislem = True
if cislo < 2:
    je_prvocislem = False
elif cislo==2:
    je_prvocislem = True
elif cislo % 2 == 0:
    je_prvocislem = False
else:
    delitel = 3
    while delitel <= math.sqrt(cislo):
        if cislo % delitel == 0:
            je_prvocislem = False
            break
        delitel+=2

if je_prvocislem:
    print(f"Číslo {cislo} je prvočíslem.")
else:
    print(f"Číslo {cislo} není prvočíslem.")
