pocet_mesicu = int(input("Zadejte počet měsíců simulace: "))

a = 0
b = 1
mesic = 1

print(f"\nSimulace růstu populace králíků pro císaře Fridricha II. na {pocet_mesicu} měsíců:\n")

while mesic <= pocet_mesicu:
    print(f"Měsíc {mesic}: {b} párů " + ("🐇" * b))
    
    dopredu = a + b
    a = b
    b = dopredu
    
    mesic += 1


