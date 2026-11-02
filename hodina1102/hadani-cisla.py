import random
tajne_cislo = random.randint(1, 20)
pokusy = 0
max_pokusy = 5
tip = 0
print(f"Hádej celé číslo mezi 1 a 20. Máš {max_pokusy} pokusů.")

while tip != tajne_cislo and pokusy <= max_pokusy:
    tip = int(input("Tipni číslo mezi 1 a 20: "))
    if tip < 1 or tip > 20:
        print("Číslo musí být mezi 1 a 20!")
        continue
    pokusy+=1
    if tip < tajne_cislo:
        print("Moje číslo je VĚTŠÍ!.")
    elif tip > tajne_cislo:
        print("Moje číslo je MENŠÍ!.")

if tip==tajne_cislo:
    print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokusy}. pokus.")
else:
    print(f"Vyčerpal jsi všechny pokusy! Moje číslo bylo {tajne_cislo}.") 
