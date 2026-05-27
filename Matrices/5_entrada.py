def ingresar_matriz():
    while True:
        try:
            filas = int(input("Ingrese el número de filas: "))
            columnas = int(input("Ingrese el número de columnas: "))
            break
        except ValueError:
            print("Error: debe ingresar números enteros.")

    matriz = []
    print("Ingrese los elementos de la matriz:")

    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    valor = float(input(f"A[{i}][{j}]: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Error: ingrese un número válido.")
        matriz.append(fila)

    return matriz


def mostrar_matriz(A):
    print("\nMatriz:")
    for fila in A:
        print(fila)
