print("Mysli si číslo od 1 do 100.")
print("Na každou odpověď reaguj m (menší),v (větší), nebo s (správně)")

minimum = 1
maximum = 100
pokusy = 0


while minimum <= maximum:
    pokusy += 1
    tip = (minimum + maximum) // 2
    odpoved = input(f"Myslíš si číslo {tip}? m, v, nebo s? ")
    if odpoved == "m":
        maximum = tip - 1
    elif odpoved == "v":
        minimum = tip + 1
    elif odpoved == "s":
        print(f"Uhodl jsem číslo {tip} na {pokusy}. pokus.")
        break
    else:
        print("Špatná odpověď. Odpověz m (menší),v (větší), nebo s (správně).")