"""1. Crie um programa que faça a leitura de dois valores: o valor do salário de um
funcionário e o percentual de aumento no salário. O programa deve calcular o
aumento e apresentar como saída o salário inicial, o percentual de aumento e o
novo valor do salário após o aumento."""

salary_value = float(input("Digite o valor do salário (número, ex: 1.000): "))
increase_percentage = float(input(f"Digite o percentual de aumento do salário "
                                  "\nem decimal, ex: 0.0, 0.1 ou 1.5:"))

new_salary_value = (salary_value * increase_percentage) + salary_value

print(f"Salário inicial: {salary_value}")
print(f"Porcentagem: {increase_percentage}")
print(f"Salário após acréscimo: {new_salary_value}")