"""2. Um grupo de professores do campus do IFRN moram em Natal, mas lecionam no
campus localizado em Currais Novos. Impactados pelo preço do combustível,
decidiram compartilhar um único carro e repartir os custos da viagem entre eles.
Semanalmente eles precisam verificar quantas pessoas irão, a distância percorrida
ao final da viagem, o preço do combustível e a média de consumo do automóvel
(quantidade de quilômetros que o carro percorre com um litro). Crie um programa
que calcule o valor individual gasto em cada viagem. As entradas e a saída do
programa estão listadas abaixo:
ENTRADAS:
    • Quantidade de pessoas
    • Distância percorrida
    • Preço do combustível
    • Média de consumo
SAÍDA
    • O valor da despesa para cada professor
EXEMPLO:
    • Quantidade de pessoas: 4
    • Distância percorrida: 300
    • Preço do combustível: 7.00
    • Média de consumo: 12
Saída: O valor da despesa para cada professor foi: 43.75"""

amount_of_people = int(input("Digite a quantidade de pessoa(s): "))
travelled_distance = float(input("Digite a distância percorrida: "))
fuel_price = float(input("Digite o preço do combustível: "))
average_comsuption = float(input("Digite a média de consumo: "))

expense_per_person = ((fuel_price * travelled_distance) / (average_comsuption)) / amount_of_people
print(f"O valor da despesa para cada professor foi: R$ {expense_per_person}")