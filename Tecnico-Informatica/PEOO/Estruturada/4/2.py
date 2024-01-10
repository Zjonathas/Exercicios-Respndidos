"""2. Crie um programa que receba uma frase do usuário e informe quantas palavras há
na frase."""

phrase = input("Digite uma frase: ")

number_of_words = len(phrase.split()) # A função split transforma a string em uma lista separando os elementos de acordo com os espaços

print(f"A quantidade de palavars na frase é: {number_of_words}")