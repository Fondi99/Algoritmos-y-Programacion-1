import os
from random import randint, sample
from colored import Fore, Style
from typing import List, Union, Dict, Tuple


def inicializar_piramide(jugadores: int) -> List[List[str]]:
    filas = jugadores + 2
    piramide = []
    for i in range(1, filas + 1, +1):
        piramide.append(['|'] * i)
    return piramide


def imprimir_piramide(piramide: List[List[str]]) -> None:
    largo = len(piramide[-1])
    i = 1
    for fila in piramide:
        print(i, " " * largo, end='')
        i += 1
        for elemento in fila:
            print(elemento, end=' ')
        print()
        largo -= 1


def añadir_palos_rojos(piramide: List[List[str]]) -> None:
    palitos_totales = int((len(piramide)) * (len(piramide) + 1) / 2)
    n_palitos_rojos = randint(int(palitos_totales * 0.2), int(palitos_totales * 0.3))
    # seleccionar un lugar aleatorio para los palitos
    palitos_rojos = sample([(i, j) for i in range(len(piramide)) for j in range(len(piramide[i]) - 1)], n_palitos_rojos)
    for i, j in palitos_rojos:
        piramide[i][j] = f"{Fore.red}|{Style.reset}"


def tirar_dados() -> int:
    return randint(1, 6)


def limpiar_pantalla() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def reorganizar_piramide(piramide: List[List[str]]) -> None:
    maxima_fila = len(piramide)
    fin_reordenamiento = True
    while maxima_fila > 1 and fin_reordenamiento:
        if len(piramide[maxima_fila - 1]) < maxima_fila:
            filas_a_mover = 1
            while len(piramide[maxima_fila - 1 - filas_a_mover]) == 0 and maxima_fila - 1 - filas_a_mover >= 0:
                filas_a_mover += 1
            if maxima_fila - 1 - filas_a_mover < 0:
                fin_reordenamiento = False
            else:
                elemento_a_mover = piramide[maxima_fila - 1 - filas_a_mover].pop(0)
                piramide[maxima_fila - 1].append(elemento_a_mover)
        if len(piramide[maxima_fila - 1]) == maxima_fila:
            maxima_fila -= 1


def manejar_evento(evento: int, piramide: List[List[str]], jugador: int, jugadores: int) -> Union[int, None, List[List[str]]]:
    if evento == 1:
        return jugador
    elif evento == 2:
        cant_max_palitos = (jugadores + 2) * (jugadores + 3) // 2
        # contar palitos en la piramide actualmente
        palitos_en_piramide = len([elemento for sublista in piramide for elemento in sublista])
        palitos_a_añadir = randint(1, len(piramide))
        if palitos_a_añadir + palitos_en_piramide > cant_max_palitos:
            palitos_a_añadir = cant_max_palitos - palitos_en_piramide
        print(f"{Fore.purple_4a}El jugador {jugador} añade {palitos_a_añadir} palitos.{Style.reset}")
        for i in range(palitos_a_añadir):
            piramide[0].append('|')
        reorganizar_piramide(piramide)
    elif evento == 3:
        print(f"{Fore.purple_4a}El jugador {jugador} congela el 20% de los palitos por 3 turnos.{Style.reset}")
        palitos_en_piramide = len([elemento for sublista in piramide for elemento in sublista])
        cant_palitos_a_congelar = int(palitos_en_piramide * 0.2)
        if cant_palitos_a_congelar < 1:
            cant_palitos_a_congelar = 1
        # seleccionar un lugar aleatorio para los palitos
        palitos_congelados = sample([(i, j) for i in range(len(piramide)) for j in range(len(piramide[i]) - 1)],
                                    cant_palitos_a_congelar)
        for i, j in palitos_congelados:
            piramide[i][j] = f"{Fore.blue}|{Style.reset}"

    elif evento == 4:
        print(f"{Fore.purple_4a}El jugador {jugador} debe elegir una fila para remover.{Style.reset}")
        fila_a_remover = int(input(f"{Fore.purple_4a}Escoge la fila que deseas remover(1 to N): {Style.reset}")) - 1
        if 0 <= fila_a_remover < len(piramide):
            piramide[fila_a_remover] = []
        reorganizar_piramide(piramide)
    elif evento == 5:
        print(
            f"{Fore.purple_4a}El jugador {jugador} crea una nueva piramide del mismo tamaño que la original.{Style.reset}")
        nueva_piramide = inicializar_piramide(jugadores)
        añadir_palos_rojos(nueva_piramide)
        return nueva_piramide
    else:
        print(f"{Fore.purple_4a}El jugador {jugador} saca 6 y no pasa nada.{Style.reset}")


def jugar(jugadores: int) -> None:
    piramide: List[List[str]] = inicializar_piramide(jugadores)
    añadir_palos_rojos(piramide)
    jugador_actual: int = 1
    turno: int = 1
    pierde_turno: List[int] = []
    congelado: int = 0
    palitos_sacados: Dict[int, int] = {}
    jugando: bool = True

    while jugando:
        limpiar_pantalla()
        print(f'--------------------------------------')
        print(f'{Fore.yellow}Ronda Actual: {turno}{Style.reset}')
        print(f"{Fore.yellow}Jugador Actual: {jugador_actual}{Style.reset}")
        if turno == congelado:
            piramide = [[palito if palito != '\x1b[38;5;4m|\x1b[0m' else '|' for palito in fila] for fila in piramide]
        reorganizar_piramide(piramide)
        if jugador_actual in pierde_turno:
            print(f"{Fore.yellow}El jugador {jugador_actual} salta su turno.{Style.reset}")
            pierde_turno.remove(jugador_actual)
        else:
            imprimir_piramide(piramide)
            palitos_a_remover: List[Tuple[int, int]] = []
            palitos_en_piramide: int = len([elemento for sublista in piramide for elemento in sublista])
            if palitos_en_piramide <= 3:
                remover_palito = int(input(f"{Fore.yellow}Cuantos palitos deseas remover?(1-{palitos_en_piramide}){Style.reset}"))
            else:
                remover_palito = int(input(f"{Fore.yellow}Cuantos palitos deseas remover?(1-3){Style.reset}"))
            palitos_sacados[jugador_actual] = palitos_sacados.get(jugador_actual, 0) + remover_palito
            sacado_de_palitos: bool = True
            while sacado_de_palitos:
                try:
                    filas: int = len(piramide)
                    fila: int = int(input(f"{Fore.yellow}Ingresa la fila(1 a {filas}): {Style.reset}")) - 1
                    if 0 <= fila < filas:
                        n_palito: int = len(piramide[fila])
                        palito: int = int(input(f"{Fore.yellow}Ingresa el palito (1 a {n_palito}): {Style.reset}")) - 1
                        if 0 <= palito < n_palito:
                            palitos_a_remover.append((fila, palito))
                            if len(palitos_a_remover) == remover_palito:
                                sacado_de_palitos = False
                except (ValueError, IndexError):
                    print(f"{Fore.yellow}Input invalido, proba de nuevo.{Style.reset}")
            ocurre_evento: bool = False
            palitos_a_remover.sort(reverse=True)
            for fila, palito in palitos_a_remover:
                if piramide[fila][palito] == '\x1b[38;5;1m|\x1b[0m':
                    ocurre_evento = True
                    del piramide[fila][palito]
                elif piramide[fila][palito] == '\x1b[38;5;4m|\x1b[0m':
                    print('Este palito no se puede remover porque esta congelado')
                else:
                    del piramide[fila][palito]
            if ocurre_evento:
                evento: int = tirar_dados()
                print(
                    f"{Fore.purple_4a}El jugador {jugador_actual} saco un palito rojo y tiro un {evento} en los dados.{Style.reset}")
                respuesta = manejar_evento(evento, piramide, jugador_actual, jugadores)
                if evento == 1:
                    jugador = manejar_evento(evento, piramide, jugador_actual, cant_jugadores)
                    print(f"{Fore.purple_4a}El jugador {jugador} pierde el proximo turno.{Style.reset}")
                    pierde_turno.append(jugador)
                if evento == 3:
                    congelado = turno + 3
                if evento == 5:
                    if respuesta:
                        piramide = respuesta
            palitos_en_piramide: int = len([elemento for sublista in piramide for elemento in sublista])
            if palitos_en_piramide == 0:
                print(f"El jugador {jugador_actual} pierde. Fin del juego!")
                for jugador, palitos_removidos in palitos_sacados.items():
                    print(f"El jugador {jugador} sacó {palitos_removidos} palitos.")
                jugando = False
            input(f'{Fore.yellow}Presiona Enter para continuar...{Style.reset}')
        jugador_actual += 1
        if jugador_actual > jugadores:
            jugador_actual: int = 1
            turno += 1


if __name__ == "__main__":
    cant_jugadores: int = int(input(f'{Fore.yellow}Ingrese la cantidad de jugadores(2 to N): {Style.reset}'))
    jugar(cant_jugadores)
