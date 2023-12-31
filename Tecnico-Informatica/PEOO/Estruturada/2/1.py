""""1. A nota final de uma disciplina no ensino médio do IFRN é resultado do cálculo da média
ponderada de quatro notas correspondentes as unidades ao longo do ano. O cálculo da média é
feito usando a expressão: (N1*2 + N2*2 + N3*3 + N4*3)/10. Sabendo que a média não pode
ser representada por um valor com casas decimais, crie um programa que recebe quatro valores
(notas de cada unidade), calcula a média e apresenta a situação final do aluno. Há três situações
possíveis para o aluno e isso depende do valor da sua média.
    • APROVADO: média maior ou igual a 60
    • RECUPERAÇÃO: média entre 20 e 50
    • REPROVADO: média abaixo de 20"""

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))

media_das_notas = (nota1 * 2 + nota2 * 2 + nota3 * 3 + nota4 * 3) / 10

if media_das_notas >= 60:
    print(f"Aluno aprovado com média de {media_das_notas}")
elif media_das_notas <= 50 and media_das_notas >= 20:
    print(f"Aluno em recuperação com média de {media_das_notas}")
elif media_das_notas < 20:
    print(f"Aluno em reprovado com média de {media_das_notas}")

