#pasar un numero en base decimal a base 6
def decimal_a_binario(numero):
    if numero == 0:
        return "0"  # Manejo del caso especial de 0

    binario = ""
    while numero > 0:
        residuo = numero % base
        binario = str(residuo) + binario
        numero = numero // base

    return binario

numero_decimal = int(input("Ingrese un número decimal: "))
base = int(input("Ingrese la base a la que desea convertir el número decimal: "))
binario_resultado = decimal_a_binario(numero_decimal)
print(f"El número binario equivalente es: {binario_resultado}")
