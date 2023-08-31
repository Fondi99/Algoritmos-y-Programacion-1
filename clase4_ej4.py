import os

palabra = ""
longitud_palabra = 0
intento01 = 0
intento02 = 0
intento03 = 0
partidas_ganadas = 0

palabra = input("Usuario A, ingresar una palabra: ")
os.system("cls")
longitud_palabra = len(palabra)
print("\nUsuario B, tendrá que adivinar la longitud de la palabra que ingresó el usuario A\n")
intento01 = int(input("Ingrese la longitud de la palabra: "))
if (intento01 == longitud_palabra):
    partidas_ganadas+=1
palabra = input("Usuario A, ingresar otra palabra: ")
os.system("cls")
longitud_palabra = len(palabra)
print("\nUsuario B, tendrá que adivinar la longitud de la palabra que ingresó el usuario A\n")
intento02 = int(input("Ingrese la longitud de la palabra: "))
if (intento02 == longitud_palabra):
    partidas_ganadas+=1
palabra = input("Usuario A, ingresar otra palabra: ")
os.system("cls")
longitud_palabra = len(palabra)
print("\nUsuario B, tendrá que adivinar la longitud de la palabra que ingresó el usuario A\n")
intento03 = int(input("Ingrese la longitud de la palabra: "))
if (intento03 == longitud_palabra):
    partidas_ganadas+=1
if partidas_ganadas ==1:
    print("WIN!")
if partidas_ganadas ==2:
    print("WIN! WIN!")
if partidas_ganadas ==3:
    print("TOTAL WINNER!")
if partidas_ganadas ==0:
    print("GAME OVER! Maybe next time!")