"""1. Crie um programa que receba uma mensagem digitada pelo usuário e informe a ele
quando o texto ultrapassar 280 caracteres."""

menssage = input("Digite uma menssagem: ")

if len(menssage) > 280: # A função len retorna um valor inteiro com o tamanho da string
    print(f"A mensagem digitada tem a quantidade de caracteres maior que 280.")
else:
    print(f"A quantidade máxima de caracteres não ultrapassou 280.")