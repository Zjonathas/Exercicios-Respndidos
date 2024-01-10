""""1. Escreva um programa que dois valores um que determina o tamanho da lista e outro que deve
ser inserido da lista. O programa deve preencher cada posição restante da lista com metade do
valor armazenado na posição anterior, conforme o exemplo abaixo. Ao final exiba o conteúdo
da lista.
Exemplo:
    Tamanho: 3
    Primeiro elemento: 100
    Segundo elemento: 100/2 = 50
    Terceiro elemento: 50/5 = 25"""

lenght = int(input("Digite o tamanho da lista: "))
first_element = float(input("Digie o primeiro valor da lista: "))
list_user = []

for i in range(lenght):
    list_user.append(first_element)
    first_element = first_element / 2

print(f"Lista: {list_user}")