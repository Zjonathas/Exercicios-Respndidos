"""5. Escreva um programa para analisar propostas de empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação
como sendo o valor da casa a comprar dividido pelo número de meses a pagar."""

valor_da_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do sálario: "))
quantidade_de_anos_a_pagar = float(input("Digite a quantidade de anos a pagar: "))

meses = quantidade_de_anos_a_pagar * 12

prestacao_mensal = valor_da_casa / meses

limite_da_parcela = salario * 0.3

if prestacao_mensal > limite_da_parcela:
    print(f"A parcela ficou R$ {prestacao_mensal:.2f} por mês e 30% do seu sálarios é {limite_da_parcela:.2f}.\n"
          f"Sendo assim, o empréstimo não será possível.")
else:
    print(f"A parcela ficou R$ {prestacao_mensal:.2f} por mês e 30% do seu sálarios é {limite_da_parcela:.2f}.\n"
          f"Sendo assim, o empréstimo será possível.")
