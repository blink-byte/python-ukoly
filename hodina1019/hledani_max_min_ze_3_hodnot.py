a = int(input("Zadej a: "))
b = int(input("Zadej b: "))
c = int(input("Zadej c: "))
#nejprve nastavím, že max i min je a
min = a
max = a
#porovnám s b
if b < min:
    min = b
elif b > max:
       max = b
#porovnám s c
if c < min:
    min = c
elif c > max:
    max = c
print("Minimální číslo:", min)
print("Maximální číslo:", max)
