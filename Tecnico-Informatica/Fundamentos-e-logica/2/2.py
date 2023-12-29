"""2. Faça um programa que recebe 2 números e informa qual é o maior, qual é o menor
ou se eles são iguais."""

number_1 = float(input("Digite um número: "))
number_2 = float(input("Digite outro número: "))

if number_1 > number_2:
    print("-" * 50)
    print(f"O número {number_1} é maior que o número {number_2}.")
    print("-" * 50)
elif number_2 > number_1:
    print("-" * 50)
    print(f"O número {number_2} é maior que o número {number_1}.")
    print("-" * 50)
else:
    print("-" * 50)
    print(f"O {number_1} e o número {number_2} são iguais.")
    print("-" * 50)


