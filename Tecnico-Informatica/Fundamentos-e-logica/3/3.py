"""3. Faça um programa que simule um jogo de adivinhação. Você mesmo fixa o número
que precisa ser adivinhado com um valor entre 1 e 10. Na sequência o programa
pergunta qual o palpite do jogador. O diferencial deste programa é que ele só deve
encerrar quando o usuário acertar o número a ser adivinhado, enquanto ele não
acertar, o programa deve permanecer perguntando o seu palpite. Para cada palpite,
o programa deve exibir uma dessas mensagens abaixo:
    a. Você acertou! - se o palpite for igual ao número inicializado
    b. Você errou por pouco - se a diferença entre o valor do palpite e o número
    inicial for menor que 3.
    c. Você passou longe - quando"""

while True:
    number_choice = int(input("Digite um número de 1 a 10 ou 100 para sair: "))
    if number_choice == 100:
        break
    guess = int(input("Dê um palpite de 1 a 10: "))

    difference = guess - number_choice
    # Evita da diferença ser negativa
    if difference < 0:
        difference = difference * -1

    if guess == number_choice:
        print("Parabéns, você acertou o número!")
    elif difference < 3:
        print(f"Você errou por pouco. A diferença foi de {difference}")
    else:
        print(f"Você passou longe. Diferença: {difference}")