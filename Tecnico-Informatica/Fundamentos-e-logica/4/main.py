"""1. O grêmio escolar está em período de eleições. Você foi requisitado para criar um sistema de
votação semelhante a uma urna eletrônica. Seu sistema precisa receber os votos nos candidatos e
exibir um boletim final com a quantidade de votos que cada um recebeu, além dos votos em
branco e nulos. Leia atentamente os requisitos do sistema abaixo e crie um programa de acordo
com a descrição.
1.1. As eleições têm apenas três candidatos que já devem estar cadastrados na hora da votação. O
sistema registrará apenas o voto de cada eleitor. Ou seja, VOCÊ, programador quem deve
informar quem são os candidatos. Use nomes fictícios ou genéricos, tipo, candidatos A, B e
C.
1.2. O sistema deve permanecer em execução recebendo os votos até que seja informada uma
opção de encerrar a votação.
1.3. O sistema tem que informar quem são os candidatos e o número de votação de cada um, além
da opção votar em branco (figura 1).
1.4. O voto só é considerado NULO quando o eleitor (usuário) digitar outro número que não seja
de nenhum candidato.
1.5. Quando o usuário informar a opção para encerrar a votação, o sistema deve apresentar o total
de votos registrados, a lista com os candidatos, a quantidade de votos que cada um recebeu e
também a quantidade de votos em branco e nulos (figura 2).
1.6. As telas do sistema não precisam ser exatamente iguais as exibidas nas figuras. Os modelos
são apenas uma referência para orientar a criação do algoritmo."""

candidate_x = 0
candidate_y = 0
candidate_z = 0
white_votes = 0
null_votes = 0

while True:
    print("#" * 50)
    print(f"Escolha uma das opções abaixo:")
    print(f"1 - Candidato x | 2 - Candidato y | 3 - Candidato z | 4 - Branco | 0 - Encerrar Votação")
    print("#" * 50)
    choice = input("- ")
    match choice:
        case '1':
            candidate_x += 1
        case '2':
            candidate_y += 1
        case '3':
            candidate_z += 1
        case '4':
            white_votes += 1
        case '0':
            break
        case _: 
            null_votes += 1

total_votes = candidate_x + candidate_y + candidate_z + white_votes + null_votes
print("~" * 50)
print("RESUMO DA VOTAÇÃO")
print("~" * 50)
print(f"Candidato x: {candidate_x}\n"
      f"Candidato y: {candidate_y}\n"
      f"Candidato z: {candidate_z}\n"
      f"Brancos: {white_votes}\n"
      f"Nulos: {null_votes}\n"
      f"Total de votos: {total_votes}\n")
print("~" * 50)