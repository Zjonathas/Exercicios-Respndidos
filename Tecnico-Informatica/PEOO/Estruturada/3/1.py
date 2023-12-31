"""1) Desenvolva um algoritmo que leia a altura de 5 pessoas. Este programa deverá calcular e mostrar:
    a) A menor altura do grupo
    b) A maior altura do grupo
    c) A média de altura"""

atual = 0
maior = 0
menor = 0

for i in range(5):
    atual = float(input("Digite uma altura: "))

    if i == 0:
        menor = atual

    if atual > maior:
        maior = atual
    elif atual < menor:
        menor = atual
print(f"Maior altura: {maior:.2f}\n"
      f"Menor altura: {menor:.2f}\n"
      f"Media: {(maior + menor + atual) / 3:.2f}\n")