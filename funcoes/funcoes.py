def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

# Solicita ao usuário o valor de n
n = int(input("Digite o valor de n para a sequência de Fibonacci: "))

# Calcula a sequência de Fibonacci
fibonacci_sequence = fibonacci(n)

# Exibe a sequência
print(f"Sequência de Fibonacci até o {n}-ésimo valor: {fibonacci_sequence}")



def inverter_string(string):
    if len(string) == 0:
        return string
    else:
        return inverter_string(string[1:]) + string[0]

string_original = input("Digite uma string para inverter: ")

string_invertida = inverter_string(string_original)

print(f"A string invertida é: {string_invertida}")

def soma_vetor_recursivo(vetor, n):
    if n <= 0:
        return 0
    else:
        return vetor[n - 1] + soma_vetor_recursivo(vetor, n - 1)

tamanho = int(input("Digite o tamanho do vetor: "))

vetor = []
for i in range(tamanho):
    elemento = int(input(f"Digite o elemento {i + 1}: "))
    vetor.append(elemento)

soma = soma_vetor_recursivo(vetor, tamanho)

print(f"A soma dos elementos do vetor é: {soma}")
def somatorioaten(n):
    if n == 1:
        return 1
    else:
        return n + somatorioaten(n - 1)

n = int(input("Digite um número inteiro positivo (N): "))

if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    resultado = somatorioaten(n)
    print(f"O somatório dos números de 1 a {n} é: {resultado}")

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

n = int(input("Digite um número inteiro para calcular o fatorial: "))

if n < 0:
    print("Por favor, digite um número inteiro não negativo.")
else:
    resultado = fatorial(n)
    print(f"O fatorial de {n} é: {resultado}")

def calcular_potencia(x, z):
    resultado = 1
    for _ in range(z):
        resultado *= x
    return resultado

x = int(input("Digite o valor de X: "))
z = int(input("Digite o valor de Z: "))

potencia = calcular_potencia(x, z)

print(f"{x}^{z} = {potencia}")

def calcular_S(N):
    S = 1.0

    fatorial = 1

    for i in range(1, N + 1):
        fatorial *= i

        if i % 2 == 0:
            S += 1 / fatorial
        else:
            S += 1

    return S

N = int(input("Digite um valor inteiro e positivo N: "))

if N < 1:
    print("Por favor, digite um valor inteiro e positivo N.")
else:
    resultado = calcular_S(N)
    print(f"O valor de S para N = {N} é: {resultado:.4f}")


def somatorio(N):
    if N < 1:
        return 0
    else:
        resultado = 0
        for i in range(1, N + 1):
            resultado += i
        return resultado

N = int(input("Digite um valor inteiro e positivo (N): "))

if N < 1:
    print("Por favor, digite um valor inteiro e positivo.")
else:
    resultado = somatorio(N)
    print(f"O somatório de 1 a {N} é: {resultado}")

def contar_divisores(N):
    if N <= 0:
        return 0

    num_divisores = 1

    for i in range(1, N // 2 + 1):
        if N % i == 0:
            num_divisores += 1

    return num_divisores

N = int(input("Digite um valor inteiro e positivo (N): "))

if N <= 0:
    print("Por favor, digite um valor inteiro e positivo maior que 0.")
else:
    num_divisores = contar_divisores(N)
    print(f"O número de divisores de {N} é: {num_divisores}")

def tabuada(N):
    for i in range(1, N + 1):
        resultado = i * N
        print(f"{i} x {N} = {resultado}")

N = int(input("Digite um valor inteiro (N): "))

if N <= 0:
    print("Por favor, digite um valor inteiro maior que 0.")
else:
    tabuada(N)
