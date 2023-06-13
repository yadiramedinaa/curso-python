import random

while True:

    aleatorio = random.randrange(0, 3) 
    elijepc = ""
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion = int(input("Elige tu opción ")) 
    
    if opcion == 1:
        elijeUsuario = "Piedra"
    elif opcion == 2:
        elijeUsuario = "Papel"
    elif opcion == 3:
        elijeUsuario = "Tijera"
    print("Elejiste: ", elijeUsuario)
    if aleatorio == 0: 
        elijePc = "Piedra"
    elif aleatorio == 1: 
        elijePc = "Papel"
    elif aleatorio == 2:
        elijePc = "Tijera"
    print("La máquina elijio: ", elijePc)
    print("...")
    if elijePc == "Piedra" and elijeUsuario == "Papel": 
        print("Ganaste, papel envuelve Piedra")
    elif elijePc == "Papel" and elijeUsuario == "Tijera": 
        print("Ganaste, Tijera corta papel") 
    elif elijePc == "Tijera" and elijeUsuario == "Piedra":
        print("Ganaste,piedra chanca tijera")
    if elijePc == "Papel" and elijeUsuario == "Piedra":
        print("perdiste,Papel envuelve piedra")
    elif elijePc == "Tijera" and elijeUsuario == "Papel":
        print("perdiste,tijera corta papel")
    elif elijePc == "Piedra" and elijeUsuario == "Tijera":
        print("perdite, piedra chanca tijera")
    elif elijePc == elijeUsuario:
        print("empate")
    
    play_again = input("quieres jugar de nuevo(s/n): ")
    if play_again.lower() != "s":
        break