"""2. Faça um programa que receba 10 notas de alunos e os insira em uma lista. Após a entrada, o
programa deve exibir:
    a) A média da turma
    b) Quantos alunos tiraram nota acima de 60
    c) Quantos alunos tiraram nota abaixo de 20
    d) Quantos alunos tiraram nota entre 21 e 59
    e) Quantos alunos tiraram nota zero"""

score_list = []
over_60 = 0
below_20 = 0
between_21_59 = 0
zeros = 0

for i in range(10):
    score_value = float(input(f"Digite a nota {i+1}: "))
    score_list.append(score_value)

for i in score_list:
    if i > 60:
        over_60 += 1
    elif i <= 20 and i > 0:
        below_20 += 1
    elif i == 0:
        zeros += 1
    else:
        between_21_59 += 1


average_score = sum(score_list) / len(score_list)

print(f"Média da turma: {average_score:.2f}\n"
      f"Alunos acima de 60: {over_60}\n"
      f"Alunos abaixo de 20: {below_20}\n"
      f"Alunos entre 21 e 59: {between_21_59}\n"
      f"Alunos com 0: {zeros}")
