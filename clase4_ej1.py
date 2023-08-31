list=[]
for i in range(5):
    num = int(input("Ingrese un numero"))
    list.append(num)
list.sort()
print("Max: ",list[0])
print("Min: ",list[4])
