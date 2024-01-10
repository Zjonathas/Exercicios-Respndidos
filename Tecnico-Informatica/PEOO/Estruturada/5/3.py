"""3. Faça um programa que receba coleta o nome e o sexo de um número X de pessoas. O programa
deve iniciar perguntando quantas pessoas são, depois receber um par de valores para cada pessoa
(nome e sexo) e adicionar o par a lista. Após finalizar as entradas, o programa deve exibir:
    a) A quantidade total de pessoas
    b) A quantidade de homens
    c) A quantidade de mulheres"""

amount_of_people = int(input("Digite a quantidade de pessoas: "))
people_info = []
number_of_man = 0
number_of_woman = 0

for i in range(amount_of_people):
    sex = input(f"Digite o sexo da pessoa {i+1}: ")
    name = input(f"Digite o nome da pessoa {i+1}: ")
    people_info.append([name, sex])

for i in people_info:
    number_of_man += i.count('Masculino')
    number_of_woman += i.count('Feminino')


total = len(people_info)

print(f"Quantidade total de pessoas: {total}\n"
      f"Quantidade de homens: {number_of_man}\n"
      f"Quantidade de mulheres: {number_of_woman}\n")