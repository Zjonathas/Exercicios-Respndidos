"""3. Elabore um programa onde o usuário pode digitar quantas palavras quiser e depois
o programa exibe uma mensagem informando quais foram a primeira a última letra
da frase."""

phrase = input("Digite uma frase: ")

"""Um elemento de uma string pode ser acessado através de seu índice
   que é colocado entre []
   Ex: phrase[0]
   Isso retornará o primeiro elemento da string.
   Os índices també podem ser acessado com sinal de -
   Ex: phrase[-1]
   
   Podemos imaginar assim:

   machado
   0123456
   -7-6-5-4-3-2-1"""

first_letter = phrase[0]
last_letter = phrase[-1]

print(f"A primeira letra da frase é: {first_letter}\n"
      f"A última letra da frase é: {last_letter}")