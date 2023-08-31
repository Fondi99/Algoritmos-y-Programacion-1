#Crear un programa que permita el almacenamiento de los datos de 4 alumnos. Estos datos deben ser, Nombre, apellido, padrón, materias aprobadas y promedio. ¿Qué sucede si fueran 80 alumnos?

cantAlumnos  = int(input("Ingrese la cantidad de alumnos: "))

alumnos = []

for i in range (cantAlumnos):
    nombre = input("Nombre del alumno: ")
    apellido = input("Apellido del alumno: ")
    padron = input("Padrón del alumno: ")
    materiasAprobadas = int(input("Materias aprobadas: "))
    promedio = float(input("Promedio del alumno: "))

    alumno={
        "nombre": nombre,
        "apellido": apellido,
        "padron": padron,
        "materias_aprobadas": materiasAprobadas,
        "promedio": promedio
    }
    alumnos.append(alumno)

print("\nDatos de los alumnos: ")
for alumno in alumnos:
    print(f"Nombre: {alumno['nombre']} {alumno['apellido']}")
    print(f"Padrón: {alumno['padron']}")
    print(f"Materias aprobadas: {alumno['materias_aprobadas']}")
    print(f"Promedio: {alumno['promedio']}")
    print("-----------------------------")