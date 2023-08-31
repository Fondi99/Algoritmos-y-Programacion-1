list=[]
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
num3 = int(input("Ingrese un numero: "))
num4 = int(input ("Ingrese un numero: "))
num5 = int(input("Ingrese un numero: "))
list.extend([num1, num2, num3, num4, num5])

list.sort()
print("Max: ",list[0])
print("Min: ",list[4])
