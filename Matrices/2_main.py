from entrada import ingresar_matriz, mostrar_matriz
from operaciones_matrices import *
from menu import mostrar_menu

def main():
    while True:
        opcion = mostrar_menu()

        if opcion == 5:
            print("Saliendo del programa...")
            break

        print("\nIngrese la primera matriz:")
        A = ingresar_matriz()

        print("\nIngrese la segunda matriz:")
        B = ingresar_matriz()

        if opcion == 1:
            resultado = sumar_matrices(A, B)
        elif opcion == 2:
            resultado = multiplicar_matrices(A, B)
        elif opcion == 3:
            resultado = hadamard_matrices(A, B)
        elif opcion == 4:
            resultado = kronecker(A, B)

        print("\nResultado:")
        mostrar_matriz(resultado)

main()
