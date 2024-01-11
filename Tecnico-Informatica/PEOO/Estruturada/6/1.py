"""1. Escreva e teste uma função que recebe um número inteiro positivo e retorna o somatório de
todos os números menores ou igual a ele. Exemplo: número = 5, somatório = 1+2+3+4+5."""

def sum_numbers_before(number):
    sum_of_numbers_before = 0
    for i in range(1, number + 1):
        sum_of_numbers_before += i 
    
    return sum_of_numbers_before

print(sum_numbers_before(3))