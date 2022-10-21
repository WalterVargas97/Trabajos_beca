print("Quieres saber tu peso en el sistema solar?, si es así, escribe en números cuanto kg pesas")

planetas = [
  ("sol", 274),
  ("luna", 1.62),
  ("mercurio", 3.7),
  ("venus", 8.87),
  ("tierra", 9.807),
  ("marte", 3.7),
  ("jupiter", 24.79),
  ("saturno", 10.44),
  ("urano", 8.87),
  ("neptuno", 11.15)
]
Peso_en_Tierra =float(input())
print("Escribe el número correspondiente con cada planeta, estrella o satelite con el que te gustaría saber tu peso. Sol = 0 , Luna = 1, Mercurio = 2, Venus = 3, Tierra = 4", "marte = 5", "jupiter = 6", "saturno = 7", "urano = 8", "neptuno = 9")
planeta_elegido = int(input())
print(planetas[planeta_elegido])
#print("El peso en {planeta[planeta_elegido]} es de: {1} kg.".format(planetas([planeta_elegido]), round(Peso_en_Tierra * planetas([planeta_elegido])) / int(9,80)))