"""2) Desenvolva um algoritmo que leia um número que especifica a quantidade de valores que serão
recebidos como entrada. O programa então recebe os valores, calcula e escreve a quantidade de
valores positivos, a quantidade de valores negativos e o percentual de valores negativos e positivos."""

quantidade_de_valores = int(input("Digite a quantidade de valores: "))

valores_positivos = 0
valores_negativos = 0
porcentagem_positivos = 0
porcentagem_negativos = 0

for i in range(quantidade_de_valores):
    valor = float(input("Digite o valor: "))

    if valor < 0:
        valores_negativos += 1
    elif valor == 0:
        continue
    else:
        valores_positivos += 1

porcentagem_negativos = (valores_negativos / quantidade_de_valores) * 100
porcentagem_positivos = (valores_positivos / quantidade_de_valores) * 100

print(f"Quantidade de valores negativos: {valores_negativos}\n"
      f"Quantidade de valores positivos: {valores_positivos}\n"
      f"Porcentagem de valores negativos: {porcentagem_negativos}\n"
      f"Porcentagem de valores positivos: {porcentagem_positivos}")