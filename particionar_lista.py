def particionar_lista(list, n):
    listita = []
    for i in range(0, len(list), n):
        listita.append(lista[i:i + n])
    print(listita)

lista=["A", "B", "C", "D", "E", "F", "G"]
particionar_lista(lista, 2)