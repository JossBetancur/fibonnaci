def fibonacci(n):
    a, b = 0, 1
    serie = []
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    return serie

def factorial(n):
    if n < 0:
        return "No existe factorial de números negativos."
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def numeros_perfectos(n):
    perfectos = []
    num = 1
    while len(perfectos) < n:
        suma = sum(i for i in range(1, num) if num % i == 0)
        if suma == num:
            perfectos.append(num)
        num += 1
    return perfectos

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

        elif opcion == "2":
            n = int(input("Ingrese un número para calcular su factorial: "))
            print("Factorial:", factorial(n))

        elif opcion == "3":
            n = int(input("Ingrese un número para verificar si es primo: "))
            print(f"{n} ES primo" if es_primo(n) else f"{n} NO es primo")

        elif opcion == "4":
            n = int(input("¿Cuántos números perfectos desea generar?: "))
            print("Números perfectos:", numeros_perfectos(n))

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("⚠ Opción inválida, intente nuevamente.")
menu()