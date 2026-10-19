a = int(input("Zadej a: "))
b = int(input("Zadej b: "))
c = int(input("Zadej c: "))

if a>b:
    p = a
    a = b
    b = p
if b>c:
    p = b
    b = c
    c = p
if a>b:
    p = a
    a = b
    b = p

print(f"{a}, {b}, {c}")