def numero_a_letras(numero):
    unidades = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
    especiales = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']
    decenas = ['veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']

    if 0 <= numero < 10:
        return unidades[numero]
    elif 10 <= numero < 20:
        return especiales[numero - 10]
    elif 20 <= numero < 100:
        decena = numero // 10
        unidad = numero % 10
        if unidad == 0:
            return decenas[decena - 2]
        else:
            return decenas[decena - 2] + ' y ' + unidades[unidad]

numero = int(input("Ingrese un número entre 0 y 99: "))
if 0 <= numero <= 99:
    print(numero_a_letras(numero))
else:
    print("Número fuera de rango")
