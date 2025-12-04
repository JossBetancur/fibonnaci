def fibonacci(n):
    a, b = 0, 1
    serie = []
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    return serie

# ------------------------- MENÚ PRINCIPAL -------------------------

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Calcular serie Fibonacci")
        print("2. Calcular factorial de un número")
        print("3. Determinar si un número es primo")
        print("4. Generar los primeros N números perfectos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            n = int(input("Ingrese cuántos números de Fibonacci desea generar: "))
            print("Serie Fibonacci:", fibonacci(n))

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("⚠ Opción inválida, intente nuevamente.")
menu()