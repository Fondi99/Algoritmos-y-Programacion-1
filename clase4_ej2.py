def hayDuplicados():
    lista=[]
    no_unicos=[]
    for i in range(5):
        x = int(input("Inserte un numero: "))
        lista.append(x)
    for i in lista:
        if i not in no_unicos:
            no_unicos.append(i)
    if len(no_unicos)==len(lista):
        print("No hay duplicados")
    else:
        print("Hay duplicados")
hayDuplicados()