import urllib.request
URL = "https://voskh.cz/envirotyden/index.php?lokalita=kutnahora"

odpoved = urllib.request.urlopen(URL)   # odkaz na objekt odpovedi serveru
pocet_dnu = 0
celkem_srazky = 0
radek = odpoved.readline()              # nacteni dat ukoncenych koncem radku

while bool(radek):
    text = radek.decode("utf-8").strip() # vrati cisty text odpovidajici cislu, napr. "10.5"
    srazka = float(text)
    if srazka >= 0:
        celkem_srazky += srazka
        pocet_dnu += 1
    radek = odpoved.readline()

odpoved.close()                         # ukonceni komunikace

print(f"Načítám srážková data z URL: {URL}")
print("=============================================")
print("VÝSLEDKY VYHODNOCENÍ SRÁŽEK")
print("=============================================")
print(f"Zpracováno dní: {pocet_dnu} ({pocet_dnu / 365} let)")
print(f"Průměrný denní úhrn: {celkem_srazky / pocet_dnu} mm/den")


