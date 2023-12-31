"""3. Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o
resultado da operação solicitada."""

numero_um = float(input("Digite um número: "))
numero_dois = float(input("Digite outro número: "))

operacao = input("Qual operação deseja realizar (+, - , *, /): ")

if operacao == "+":
    print(f"A soma dos númeors {numero_um} e {numero_dois} é igual a {numero_um + numero_dois}")
elif operacao == "-":
    print(f"A subtração dos númeors {numero_um} e {numero_dois} é igual a {numero_um - numero_dois}")
elif operacao == "*":
        print(f"A multiplicação dos númeors {numero_um} e {numero_dois} é igual a {numero_um * numero_dois}")
elif operacao == "/":
        print(f"A divisão dos númeors {numero_um} e {numero_dois} é igual a {numero_um / numero_dois}")
else:
    print("Operação inválida.")