"""3. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 150,00. Quando o usuário
informar o tamanho da área a ser pintada, o programa precisa calcular (e informar esses valores
na saída) a quantidades de latas de tinta a serem compradas e o preço total da compra. Obs.:
somente são vendidas latas inteiras, então não dá para comprar duas latas e meias, por exemplo."""


import math # Será usado para arredondar os valores para cima com a função ceil

# Solicitar o tamanho em metros quadrados
tamanho_em_metros_quadrados = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

# Preco das latas e  tamanho
preco_lata_de_tinta = 150
capacidade_lata_de_tinta = 18

# Cobertura que 1 litro pinta
area_que_um_litro_pinta = 3


quantidade_de_litros = tamanho_em_metros_quadrados / 3 # Calculo para descobrir a quantidade de litros necessário
quantidade_de_latas_de_tintas = quantidade_de_litros / capacidade_lata_de_tinta # Cálculo para descobrir a quantidade de latas

valor_a_pagar = math.ceil(quantidade_de_latas_de_tintas) * preco_lata_de_tinta # Valor total

print(f"Quantidade de latas de tinta: {math.ceil(quantidade_de_latas_de_tintas)}\n"
      f"Valor total: R$ {valor_a_pagar:.2f}")
