# Função para calcular os coeficientes do polinômio de Newton usando diferenças divididas vistas em aula
def newton_divided_differences(x, y):
    # Determina o número de pontos
    n = len(x)

    # Inicializa a lista de coeficientes com zeros
    coef = [0] * n

    # Define o primeiro coeficiente como o primeiro valor de y
    coef[0] = y[0]

    # Loop para calcular as diferenças divididas e atualizar a lista de coeficientes
    for i in range(1, n):
        for j in range(n - i):
            y[j] = (y[j + 1] - y[j]) / (x[j + i] - x[j])

        coef[i] = y[0]

    # Retorna a lista de coeficientes
    return coef


# Função para resolver o polinômio de Newton utilizando os coeficientes e valores de x
def resolver(x, fx):
    # Calcula e imprime os coeficientes usando a função newton_divided_differences
    print(newton_divided_differences(x, fx))


# Exemplo de uso em problemas da aula teórica
print("Exercícios da aula teórica: 4)")
print("1)")
resolver([1.0, 1.3, 1.6, 1.9, 2.2], [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623])

print("\n2)")
resolver([-0.1, 0.0, 0.2, 0.3], [5.30000, 2.00000, 3.19000, 1.00000])

print("\nExercício 5):")
print("1)")
resolver([-2, -1, 0, 1, 2, 3], [1, 4, 11, 16, 13, -4])

print("\n2)")
resolver([-2, -1, 0, 1, 2], [-1, 3, 1, -1, 3])

