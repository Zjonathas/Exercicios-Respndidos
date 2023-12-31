"""3) Escreva um programa que leia um número inteiro e divida-o por dois (sucessivamente) até que o
resultado seja 0. Deve ser impresso o resto de cada divisão, considerando que as divisões serão
inteiras."""

numero = int(input("Digite um número: "))

while (numero != 0):
    numero = numero // 2
    resto = numero % 2
    print("#" * 20)
    print(f"Resultado: {numero}\n"
          f"Resto: {resto}")