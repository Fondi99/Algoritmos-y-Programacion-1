def ejercicio_2(valor):
    list = [10,20,50,100,200,500,1000]
    aux_list = sorted(list, reverse=True)
    diccionario = {}
    for i in aux_list:
        resto = valor%i
        key = valor//i
        valor = resto
        diccionario[i] = key
    
    diccionario = dict(sorted(diccionario.items(), reverse=True))
    print(diccionario)

valor = int(input("Ingrese el valor que quiere dividir en billetes: "))
ejercicio_2(valor)