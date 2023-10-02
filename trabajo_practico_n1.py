from random import randint, sample


def cant_minima_palitos(jugadores):
    return int((jugadores + 2) * (jugadores + 3) / 2)


def imprimir_piramide(palitos):
    n = 1
    numero_triangular = 1
    while numero_triangular <= palitos:
        n += 1
        numero_triangular = n * (n + 1) // 2

    print("Piramide de palitos:")
    print(n)
    for i in range(n):
        print(" " * (n - i - 1) + "| " * i)


def imprimir_matriz(matriz):
    m = [[(1, False)], [(2, False)], [(4, True), (5, True), (6, False)], [(7, False), (8, False), (9, False), (10, True)]]
    n = len(m)
    for i in range(n):
        spaces = " " * (n - i - 1)
        row_elements = " ".join("|" if not elem[1] else " " for elem in matriz[i])
        print(spaces + row_elements)
    print()
    # n = len(m) + 1
    # for i in range(n):
    #     spaces = " " * (n - i - 1)
    #     bars = "| " * i
    #     print(spaces + bars)
    # print()


def inicializar_matriz(n):
    p = cant_minima_palitos(n)
    lista_enteros = []
    for i in range(1, p + 1):
        lista_enteros.append(i)
    matriz = []
    fila_actual = []
    for i in lista_enteros:
        fila_actual.append(i)
        if len(fila_actual) == len(matriz) + 1:
            matriz.append(fila_actual)
            fila_actual = []
    matriz_nueva = []
    for i in matriz:
        fila_resultado = []
        for j in i:
            fila_resultado.append((j, False))
        matriz_nueva.append(fila_resultado)
    imprimir_piramide(p)
    imprimir_matriz(matriz_nueva)
    return matriz_nueva


def main():
    numero_jugadores = int(input("Ingrese el numero de jugadores: "))
    minima_palitos = cant_minima_palitos(numero_jugadores)
    # Cantidad de palitos rojos en la piramide
    rojos = randint(int(minima_palitos * 0.2), int(minima_palitos * 0.3))
    matriz_piramide = inicializar_matriz(numero_jugadores)
    posiciones_false = [(fila, indice) for fila, fila_valores in enumerate(matriz_piramide) for indice, valor in
                        enumerate(fila_valores) if not valor[1]]
    posiciones_a_cambiar = sample(posiciones_false, rojos)

    # Setear en matriz los palitos rojos
    for fila, indice in posiciones_a_cambiar:
        matriz_piramide[fila][indice] = (matriz_piramide[fila][indice][0], True)
    print(matriz_piramide)
    while minima_palitos > 0:
        palitos = []
        while True:
            palito_remover = input("Ingrese palitos que desea remover: ")
            if palito_remover.split() in palitos:
                print("Ya estas removiendo ese palito")
                continue
            palitos.append(palito_remover.split())
            if len(palitos) == 3:
                break
            remover = input("Desea remover otro mas?(s/n)")
            if remover.lower() != "s":
                break
        dados = False
        palitos.sort(reverse=True)
        for i in palitos:
            fila = int(i[0]) - 1
            columna = int(i[1]) - 1
            if matriz_piramide[fila][columna][1]:
                dados = True
            minima_palitos -= 1
            matriz_piramide[fila].pop(columna)
        if dados:
            dado = randint(1, 6)
            if dado == 1:
                print("El jugador pierde su próximo turno")
            elif dado == 2:
                print("Se agregan palitos")
            elif dado == 3:
                print("Se bloquean 20%")
            elif dado == 4:
                print("Bomba")
            elif dado == 5:
                print("Nueva Piramide")
            else:
                break
            print("Siguiente Turno:")


main()
