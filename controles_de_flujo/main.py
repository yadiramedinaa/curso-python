# ##COMVERCIONES STRING NUMEROS
# numero="10"
# numeroCombertido=int(numero)
# print(type(numero))
# print(type(numero))

# flotanteString="10"
# floteanteNumero=float(flotanteString)

# print(flotanteString)
# print(flotanteString)

# numeroEntero=20
# numeroSteing=str(numeroEntero)

# print(type(numeroEntero))
# print(type(numeroSteing))

# ##controles de flujo
# ##los programas se manejan de manera secuencial
# nombre="yadira"
# mensaje="hola feli"
# print(mensaje)
# print(nombre)
# ##control de flujo nos permite cortar 
# #condicionales 
# #que se realiza algo si se cumple cierta condicion 
# ###bloque
# ###cuando nosotros utilicemoscualquier control de flujo o funciones el codigo que se debe ejecutar despues debera estar 
# ###definida por bloques o identaciones 
# ##1.introduccion 
# ##1.1 otro consepto
# ##1.2 otro consepto
# ##1.2.1 este es de arriba 
# ##condicion 1
# ##si se cumple la condicion ejecuta esto
# ##condicion 2
# ##si se cumple la condicion 2 se ejecuta esto si es verdad :
# print("es verdad")
# suma=10+20
# multiplicacion=5*20
# print("otra cosa")
# if True:
# print("estoy fuera del false")


# ##match apellido:
# ##case apellido if apellido[2]=="e":
# ##print(f"bienvenida")
# ##case _:
# ##print ("tu no heres de esta raza,eres")
# ##BUCLES
# condicion=2
# while condicion<21 :
#     print(condicion)
#     condicion=condicion+2

# edad=0
# while edad !=20:
#     edad=int(input("ingrese edad"))

# nombre=" "
# while nombre !="si ":
#     nombre=input("como te llamas: ")

# while True:
#     nombre=input("como te llamas: ")
#     if nombre == "si":
#         break
# for numero in range(0,10):
#     print(numero)

# vocales=["a","e","i","o""u"]
# print(vocales[0])
# print(vocales[1])
# print(vocales[2])

# vocales=("a","e","i","o","u")
# for numero in range(0,5):
#     print(vocales[numero])
# for vocal in vocales:
#     print(vocal)

##crear un lista de 5 colores cada color que iteres tendra que mostrar 
##por consola, solo cuando encuentre el color rojo mostrara el mensaje 
##de color encontrado y se terminara la ejecucion 

# colores=["azul","amarillo","rojo","negro","blanco"]

# for color in colores:
#     if color == "rojo":
#         print ("encontado")
#         break
#     print (color)

# lista=[]
# print(lista)
# primerDato=input("ingresa una fruta: ")
# lista.append(primerDato)
# print(lista)
# segundoDato=input("ingresa una segunda fruta: ")
# lista.append(segundoDato)
# print(lista)

##crear un programa que me deje ingresar datos en una lista vacia
##en caso el usuario ingrese la palabra "si" el programa dejara
##de pedir datos y me  mostrara la lista con todos los datos ingresados 

# lista=[]
# numeros=input("ingresa un numero: ")
# while numeros!="si":
#     lista.append(numeros)
#     numeros=input("ingresa un numero: ")
# print(lista)

# lista =[]
# condicion=1
# while condicion:
#     pedirDato=input("ingrese un dato: ")
#     if pedirDato == "si":
#         condicion=0
#     lista.append(pedirDato)
# print(lista)


# lista=[]
# for dato in range(5):
#     dato=input("ingrese un dato: ")
#     lista.append(dato)
# print(lista)


# lista=[]

# while len(lista) < 5:
#     ingresaDato=input("ingresa un dato: ")
#     lista.appent(ingresaDato)

# print(f"""
#     ==================================
#     los datos ingresados son {lista})
#     ==================================
#     """)



##pedir al usuario un numero luego generar la tabla de multiplicar de dicho numero del 1 hasta el 12
#entrada=5
#1*5=5
#2*5=10
#3*5=15

#3*12=36

# tablaDe=int(input("ingresa un numero: "))
# for numero in range(1,13):
#     resultado=numero*tablaDe
#     print(f"{numero} * {tablaDe} = {resultado}")

#2 = 2*1 = 2
#3 = 3*2*1 = 6
#4 = 4*3*2*1 = 24
#5 = 5*4*3*2*1 = 120

## un programa que me pida un numero y me calcule su factorial
#ejemplo si ingreso 5
## de salida me debera imprimir 120

#numero=int(input("ingrese el numero: "))
#factorial=1
#for num in range(1,numero+1):
#    factorial=factorial*num
#    print(factorial)
#print(factorial)

##mostrar la sucecion fobocci de los 10 primeros numeros


##pedir a un usuario una lista de 5 elemtos si en la listacontiene la palabra disco 
##mostrar la palabra y la ubicacion de su indice positivo

#lista=[1,2,4"disco",6]

#disco
#se encuentra en el indice numero 3 


#lista=[]
#while len(lista)<5:
#print(lista)
#dato=input("ingresa un dato:")
#lista.appent(dato)
#print(lista)

lista=[]
indice=0
palabra=""
while len(lista)<5:
    dato=input("ingresa un dato:")
    lista.append(dato)
for texto in range(0,len(lista)):
    if lista[texto] == "disco":
        palabra=lista[texto]
        indice=texto
print(f"""el texto disco se encuentra en el indice hola {indice}
      y el texto es {palabra}
      """)
