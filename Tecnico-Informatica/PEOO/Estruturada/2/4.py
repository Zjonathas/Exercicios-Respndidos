"""4. A conta de água é calculada usando faixas de consumo. Quanto maior é o consumo mais caro é
o valor do metro cúbico que é pago. Crie um programa que recebe a quantidade de água
consumida na residência e apresenta o valor total da conta. As faixas de valores e o preço do
metro cúbico de cada faixa estão listados abaixo:
    • 0 a 30 m3 - R$ 5,00
    • 31 a 50 m3 - R$ 7,00
    • 51 a 100 m3 - R$ 9,00
    • Acima de 100 m3 - R$ 10,00"""

quantidade_de_agua_consumida = float(input("Digite a quantidade de água consumida: "))

preco1 = 5
preco2 = 7
preco3 = 9
preco4 = 10

if quantidade_de_agua_consumida <= 30:
    print(f"Valor total a pagar: R$ {quantidade_de_agua_consumida * preco1}")
elif quantidade_de_agua_consumida <= 50:
    print(f"Valor total a pagar: R$ {quantidade_de_agua_consumida * preco2}")
elif quantidade_de_agua_consumida <= 100:
    print(f"Valor total a pagar: R$ {quantidade_de_agua_consumida * preco3}")
else:
    print(f"Valor total a pagar: R$ {quantidade_de_agua_consumida * preco4}")