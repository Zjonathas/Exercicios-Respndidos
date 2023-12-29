"""3. Faça um programa que simule um jogo de adivinhação. Você mesmo inicializa o
número a ser adivinhado com um valor entre 1 e 10. Na sequência o programa
pergunta qual o palpite do jogador. O programa deve apresentar uma das três
respostas ao jogador:
a. Você acertou! - se o palpite for igual ao número inicializado
b. Você errou por pouco - se a diferença entre o valor do palpite e o número
inicial for menor que 3.
c. Você passou longe - quando a diferença entre o palpite e o número inicial
for maior ou igual a 3"""

number_choice = int(input("Digite um número de 1 a 10: "))
guess = int(input("Dê um palpite de 1 a 10: "))

# Evita da diferença ser negativa
if (guess - number_choice) < 0:
    diference = ((guess - number_choice) * (-1))
else:
    diference = guess - number_choice


if guess == number_choice:
    print("Parabéns, você acertou o número!")
elif diference < 3:
    print(f"Você errou por pouco. A diferença foi de {diference}")
else:
    print(f"Você passou longe. Diferença: {diference}")