""""1. Faça um programa que imprima indefinidamente a frase: A disciplina de
algoritmos é a melhor. \o/. O programa só encerra quando você digitar “sim”."""

word = ''

while(word != 'sim'):
    word = input("Digite algo: ").lower()
    print("A disciplina de algoritmos é a melhor. \o/.")