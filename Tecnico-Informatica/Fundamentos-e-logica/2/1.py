"""1. Faça um programa que receba um número de um usuário e exiba na tela se ele é
par ou ímpar."""

number = int(input("Digite um número inteiro: "))

# Verificação se é impar ou par
if number // 2 == 0:
    print(f"O número {number} é par!")
else:
    print(f"O número {number} é ímpar!")
