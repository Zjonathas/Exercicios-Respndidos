"""6. Gorjeta, Imposto e Total Pago – Crie um algoritmo para calcular o valor a ser pago por pessoa
em um restaurante. O usuário precisa informar o valor consumido e a quantidade de pessoas para
dividir a conta. A partir desse valor, o algoritmo deverá calcular o valor da gorjeta (10% sobre o
valor consumido), dos impostos (7%) e o total a ser pago (valor do consumo mais os valores da
gorjeta e dos impostos). Ao final, o algoritmo deverá exibir cada um desses valores, o total, a
quantidade de pessoas e o valor por pessoa."""

valor_consumido = float(input("Digite o valor consumido: "))
quantidade_de_pessoas = int(input("Digite a quantidade de pessoas para dividir a conta: "))

porcentagem_gorgeta = 0.1
gorjeta = valor_consumido * porcentagem_gorgeta

porcentagem_imposto = 0.07
imposto = valor_consumido * porcentagem_imposto

total_a_ser_pago = valor_consumido + gorjeta + imposto

valor_por_pessoa = total_a_ser_pago / quantidade_de_pessoas

print(f"Valor consumido: {valor_consumido:.2f}\n"
      f"Quantidade de pessoas: {quantidade_de_pessoas}\n"
      f"Gorgeta: R$ {gorjeta:.2f}\n"
      f"Imposto: R$ {imposto:.2f}\n"
      f"Valor por pessoa: {valor_por_pessoa:.2f}\n"
      f"Total: R$ {total_a_ser_pago:.2f}\n")

