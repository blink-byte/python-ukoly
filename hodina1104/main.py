print("Mysli si číslo od 1 do 100.")
print("Na každou odpověď reaguj menší, větší, nebo správně")

minimum= 1
maximum = 100
pokusy = 0


while minimum <= maximum:
    pokusy += 1
    tip = (minimum + maximum) // 2
    odpoved = input(f"Myslíš si číslo {tip}? menší, větší, nebo správně? ")
    if odpoved == "menší":
        maximum = tip - 1
    elif odpoved == "větší":
        minimum = tip + 1
    elif odpoved == "správně":
        print(f"Uhodl jsem číslo {tip} na {pokusy}. pokus.")
        break
    else:
        print("Špatná odpověď. Odpověz menší, větší, nebo správně.")