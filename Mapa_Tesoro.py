
Game_Over = print("Perdiste")

print("Bienvenido a la isla. Tu misión será  encontrar el tesoro")
print("Encontrarás muchos retos y decisiones que tomar, ¡Mucha Suerte!")
print("¡Oh oh! Te has encontrado con barba negra, pero aún no te ha visto.")
print(" Escribe tu decisión  ¿Decides huir o enfrentarlo?")
respuesta1 = input()
if respuesta1.lower() == "huir": ##or "ESCONDERTE" or "Esconderte":
    print("Te has encontrado con un mapa del tesoro")
    
else:
    
    print("Hey aventurero, creo que no entiendes quien manda acá, Barba negra te ha apuñalado con su sable.")
    Game_Over = exit(print("Perdiste"))
print("¿Leer el mapa o ignorar el mapa?")
respuesta2 = input()
if respuesta2.LOWER() == "ignorar":
    print("escuchaste un grito de auxilio, parece que es una damisela en apuros")
else:
    print("El mapa estaba envenenado. Muere lenta y dolorosamente.")
    Game_Over = exit(print("Perdiste"))
print("¿Buscar el origen del grito o seguir adelante?")
respuesta3 = input()
if respuesta3.LOWER() == "buscar el origen del grito":
    print("Es una princesa, te advierte que no sigas adelante porque hay un hueco, la liberas.")
else:
    print("Caiste en el agujero")
    Game_Over = exit(print("Perdiste"))
print("Recorren el camino juntos hasta llegar al lago")
respuesta4 = input()
print("¿Quieres nadar o rodear?")
if respuesta4.lower() == "rodear":
    print("Se encuentran cansados")
else:
    print("Atacado por una tribu")
    Game_Over = exit(print("Perdiste"))
respuesta5 = input()
print("¿Quieres descansar o seguir?")
if respuesta5.lower() == "Descansar":
    print("Esperan un rato y mientras hablan con la damisela encuentran muchas cosas en comun")
else:
    print("Habia un tigre en los alrededores y los ataca")
    Game_Over = exit(print("Perdiste"))
respuesta6 = input()
print("¿Seguir descansando o continuar?")
if respuesta6.lower() == "continuar":
    print("Encuentran una choza")
else:
    print("Un cazador furtivo los confunde con un leopardo y les dispara. Se mueren.")
    Game_Over = exit(print("Perdiste"))
respuesta7 = input()
print("¿Entrar o seguir?")
if respuesta7.lower() == "entrar":
    print("Hay comida, un tesoro, cama, una television. Tu y la damisela se quedan a vivir alli felizmente.")
    print("Ganaste")
else:
    print("Te perdiste en la isla")
    Game_Over = exit(print("Perdiste"))

