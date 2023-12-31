"""'5) Os números de Fibonacci formam uma sequência em que cada número é igual à soma dos dois
anteriores. Os dois primeiros números são, por definição, iguais a 1. Veja o exemplo a seguir:
Ex.: 1, 1, 2, 3, 5, 8, 13...
Escreva um programa que carregue um valor N pelo teclado e imprima os N primeiros números da
sequência de Fibonacci;"""

sequencia_quantidade = int(input("Digite quantos a qauntidade de números para fazer a sequência de Fiobonacci: "))

atual = 0
ultimo = 1
penultimo = 0

for i in range(sequencia_quantidade):
    atual = ultimo + penultimo
    penultimo = ultimo
    ultimo = atual
    print(atual)