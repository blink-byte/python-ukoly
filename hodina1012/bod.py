# kontrola, zda se bod nachází v zadané oblasti

x1_oblast = 4
y1_oblast = 2
x2_oblast = 9
y2_oblast = 7

xb = int(input("Zadej souřadnici x bodu: "))
yb = int(input("Zadej souřadnici y bodu: "))

if xb >= x1_oblast and xb <= x2_oblast and yb >= y1_oblast and yb <= y2_oblast:
    print("Bod se nachází v oblasti.")
else:
    print("Bod se nenachází v oblasti.")

if xb == x1_oblast or xb == x2_oblast or yb == y1_oblast or yb == y2_oblast:
    print("Bod se nachází na hranici.")
else:
    print("Bod se nenachází na hranici.")


