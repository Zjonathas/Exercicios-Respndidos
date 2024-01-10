"""5. Faça um programa que lê uma string e exibe “Palíndromo” caso a string seja um
palíndromo e “Não é palíndromo” caso não seja. Assuma que a entrada não tem
acentos e que todas as letras são minúsculas.
Obs: Um palíndromo é uma palavra ou frase, que é igual quando lida da esquerda
para a direita ou da direita para a esquerda (espaços em brancos são descartados).
Exemplos: “arara”, “reviver”, “mega bobagem”, “anotaram a data da maratona”."""

word = input("Digite uma palavra: ")

reverse = word[::-1] # Para inverter uma string no python usamos [::-1]

if reverse == word:
    print(f"Palavara: {word}\n"
          f"Palavara invertida: {reverse}\n"
          f"É palíndromo!")
else:
    print(f"Palavara: {word}\n"
          f"Palavara invertida: {reverse}\n"
          f"NãO é palíndromo!")