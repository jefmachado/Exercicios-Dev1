from exercicios import *

def exibir_menu():
    print("Menu:")
    print("1. Media de valores impares")
    print("2. lê um numero e mostre uma saida de acordo com o mesmo")
    print("3. multiplos de 3 e 13")
    print("4. de 1000 a 1999 apresenta os numero que divididos por 11 que o resto é 5")
    print("5. algoritimo  que solicita numeros até um valor negativo ser informa")
    print("6. GreNais")
    print("7. Sair")

while True:
    exibir_menu()
    escolha = input("Escolha uma opção (1-6): ")

    if escolha == '1':
        mediaImpar()
    elif escolha == '2':
        leNumero()

    elif escolha == '3':
        multiplos3a13()

    elif escolha == '4':
        divididospor11comresto5()

    elif escolha == '5':
        valormaioremeenor()

    elif escolha == '6':
        grenal()

    elif escolha == '7':
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 6.")

