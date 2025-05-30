# Calculadora com Python

def calculator():
    print("Bem Vindo!")
    print("Selecione a Operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")  # Corrigido typo aqui também
    print("4. Divisão")

    while True:
        escolha = input("Selecione um operador (1/2/3/4): ")

        if escolha in ('1', '2', '3', '4'):
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))  # Corrigido typo aqui

            if escolha == '1':
                resultado = num1 + num2
                operacao = "Adição"
            elif escolha == '2':
                resultado = num1 - num2
                operacao = "Subtração"
            elif escolha == '3':
                resultado = num1 * num2
                operacao = "Multiplicação"
            elif escolha == '4':
                if num2 == 0:
                    print("Erro! Divisão por zero.")
                    continue
                resultado = num1 / num2
                operacao = "Divisão"

            print(f"{operacao} de {num1} e {num2} = {resultado}")
        else:
            print("Entrada inválida")

        prox_calculo = input("Deseja fazer outra operação? (sim/não): ")
        if prox_calculo.lower() != 'sim':
            break

    print("Até logo!")

# Para usar a função:
calculator()