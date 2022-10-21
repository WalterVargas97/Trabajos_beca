print("Quieres saber tu peso en el sistema solar?, si es así, escribe en números cuanto kg pesas")

planetas =[
  ("sol", 274),
  ("luna", 1,62),
  ("mercurio", 3,7),
  ("venus", 8,87),
  ("tierra", 9,807),
  ("marte", 3,7),
  ("jupiter", 24,79),
  ("saturno", 10,44),
  ("urano", 8,87),
  ("neptuno", 11,15)
]
Peso_en_Tierra =float(input())
for planeta in planetas:
  print("El peso en {0} es de: {1} kg.".format(planeta[0],(round(Peso_en_Tierra * planeta[1] / 9,80))))