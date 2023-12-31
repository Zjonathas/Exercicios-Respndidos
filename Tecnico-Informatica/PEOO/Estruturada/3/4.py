"""4) Escreva um programa que leia um número X e a seguir:
    a) leia uma lista de números, com o término da lista ocorrendo apenas quando a soma de dois
    números consecutivos lidos na lista for igual a X.
    Exemplo:
    • número inicial lido: 50
    • condição de parada: números que lidos em sequência e somados resultem em 50: (20 30), (2
    48), (13 37), etc."""

x = int(input("Digite um número: "))

numero_inicial_da_lista = int(input("Digite o número inicial da lista: "))

while True: 
    numero2 = int(input("Digite outro número: "))

    if (numero_inicial_da_lista + numero2) == x:
        print(f"Loop parado. {numero_inicial_da_lista} + {numero2} = {x}")
        break
    else:
        numero_inicial_da_lista = numero2