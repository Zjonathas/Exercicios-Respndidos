"""4. Escreva um programa que recebe uma string S e dois inteiros i e j. O programa
então exibe a substring S[i, j]. O programa deve verificar se os números digitados
não ultrapassam o tamanho do texto. Caso isso ocorra, o programa deve solicitar
novamente os números."""

S = input("Digite uma string: ")

i = 0
j = 0

while True:
    i = int(input("Digite um índice: "))
    j = int(input("Digite outro índice: "))
    
    if i > len(S):
        print(f"O valor {i} é maior que o tamanho da sting ({len(S)})")
        continue # Faz com que o laço volte para o ínicio e não execute o que está abaixo.
    
    break

print(f"Sub string: {S[i:j]}")
