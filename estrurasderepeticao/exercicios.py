def mediaImpar():
    soma_impares = 0
    contagem_impares = 0
    for i in range(10):
        numero = int(input("Digite um número inteiro: "))

        if numero % 2 != 0:
            soma_impares += numero
            contagem_impares += 1
    if contagem_impares > 0:
        media_impares = soma_impares / contagem_impares
        print(f"A média dos números ímpares é: {media_impares:.2f}")
    else:
        print("Nenhum número ímpar foi inserido.")

def leNumero():
    numero = int(input("Digite um número inteiro: "))
    numero_str = str(numero)
    resultado = numero_str * numero
    print(resultado)

def multiplos3a13():
    for numero in range(100, 501):

        if numero % 3 == 0 or numero % 13 == 0:
            print(numero)

def divididospor11comresto5():
    for numero in range(1000, 2000):
        if numero % 11 == 5:
            print(numero)

def valormaioremeenor():
    # Inicialize variáveis
    maior_valor = float('-inf')
    menor_valor = float('inf')
    soma_valores_pares = 0
    soma_valores_impares = 0
    count_valores_maiores_50 = 0
    count_valores_maiores_20 = 0
    soma_valores_pares_entre_50_e_150 = 0
    total_valores_digitados = 0

    while True:
        numero = float(input('Digite um número (digite um valor negativo para sair): '))

        if numero < 0:
            break

        if numero > maior_valor:
            maior_valor = numero

        if numero < menor_valor:
            menor_valor = numero

        if numero % 2 == 0:
            soma_valores_pares += numero

        if numero % 2 != 0:
            soma_valores_impares += numero

        if numero > 50:
            count_valores_maiores_50 += 1

        if numero > 20:
            count_valores_maiores_20 += 1

        if 50 <= numero <= 150 and numero % 2 == 0:
            soma_valores_pares_entre_50_e_150 += numero

    if total_valores_digitados > 0:
        media_valores_impares = soma_valores_impares / (total_valores_digitados - count_valores_maiores_50)
        percentagem_valores_maiores_20 = (count_valores_maiores_20 / total_valores_digitados) * 100
        media_valores_pares_entre_50_e_150 = soma_valores_pares_entre_50_e_150 / count_valores_maiores_50

        print(f"O maior valor inserido foi: {maior_valor}")
        print(f"O menor valor inserido foi: {menor_valor}")
        print(f"A soma dos valores pares é: {soma_valores_pares}")
        print(f"A média dos valores ímpares é: {media_valores_impares}")
        print(f"Quantidade de números maiores que 50: {count_valores_maiores_50}")
        print(f"Percentagem de valores maiores que 20: {percentagem_valores_maiores_20:.2f}%")
        print(f"A média dos valores pares entre 50 e 150 é: {media_valores_pares_entre_50_e_150:.2f}")
        print(f"O total de valores digitados foi: {total_valores_digitados}")
    else:
        print("Nenhum número foi inserido.")

def grenal():
    # Inicialize as variáveis de estatísticas
    vitorias_inter = 0
    vitorias_gremio = 0
    empates = 0
    total_grenais = 0

    while True:
        gols_inter = int(input("Digite o número de gols marcados pelo Internacional: "))
        gols_gremio = int(input("Digite o número de gols marcados pelo Grêmio: "))

        if gols_inter > gols_gremio:
            vitorias_inter += 1
        elif gols_gremio > gols_inter:
            vitorias_gremio += 1
        else:
            empates += 1

        total_grenais += 1

        resposta = int(input("Novo GRE-NAL? 1.Sim 2.Não: "))

        if resposta != 1:
            break

    print("== Estatísticas dos GRE-NAIS ==")
    print(f"Total de GRE-NAIS: {total_grenais}")
    print(f"Vitórias do Internacional: {vitorias_inter}")
    print(f"Vitórias do Grêmio: {vitorias_gremio}")
    print(f"Empates: {empates}")

    if vitorias_inter > vitorias_gremio:
        print("O Internacional venceu o maior número de GRE-NAIS.")
    elif vitorias_gremio > vitorias_inter:
        print("O Grêmio venceu o maior número de GRE-NAIS.")
    else:
        print("Não houve um vencedor claro nos GRE-NAIS.")


