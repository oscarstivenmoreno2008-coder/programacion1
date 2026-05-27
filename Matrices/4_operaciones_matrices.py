def sumar_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Error: las matrices deben tener el mismo tamaño."

    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] + B[i][j])
        resultado.append(fila)

    return resultado


def multiplicar_matrices(A, B):
    if len(A[0]) != len(B):
        return "Error: columnas de A deben ser iguales a filas de B."

    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(B[0])):
            suma = 0
            for k in range(len(B)):
                suma += A[i][k] * B[k][j]
            fila.append(suma)
        resultado.append(fila)

    return resultado


def hadamard_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Error: las matrices deben tener el mismo tamaño."

    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] * B[i][j])
        resultado.append(fila)

    return resultado


def kronecker(A, B):
    resultado = []

    for filaA in A:
        for i in range(len(B)):
            fila_resultado = []
            for elementoA in filaA:
                for elementoB in B[i]:
                    fila_resultado.append(elementoA * elementoB)
            resultado.append(fila_resultado)

    return resultado
