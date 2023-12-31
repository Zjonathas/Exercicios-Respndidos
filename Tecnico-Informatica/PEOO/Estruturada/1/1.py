"""1. Escreva um algoritmo que calcule e exiba o resultado para a expressão D abaixo. Seu programa
deve receber do usuário valores para A, B e C."""

# criação de variáveis A, B e C

a =  float(input("Digite o valor de A: "))
b =  float(input("Digite o valor de B: "))
c =  float(input("Digite o valor de C: "))


# Separando a variável R e S, para ficar mais legível
r = (a + b) ** 2
s = (b + c) ** 2

# Agora juntando tudo na variável D
d = (r + s) / 2

print(f"O resultado da operação é {d}")