hodina = int(input("Zadejte hodinu (0–23): "))

if hodina < 0:
  print("Hodina nemůže být záporná.")
elif hodina >= 24:
  print("Zadávejte platné hodiny.")

else:
  if hodina < 6:
    print("Dobrou noc")
  elif hodina < 10:
    print("Dobré ráno")
  elif hodina < 12:
    print("Dobré dopoledne")
  elif hodina == 12:
    print("Dobré poledne")
  elif hodina < 18:
    print("Dobré odpoledne")
  elif hodina < 23:
    print("Dobrý večer")  
  else:
    print("Dobrou noc")