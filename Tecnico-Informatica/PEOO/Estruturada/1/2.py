"""2. A nota final de uma disciplina no ensino médio do IFRN é resultado do cálculo da média
ponderada de quatro notas correspondentes aos quatro bimestres usuais. As notas dos bimestres
possuem “pesos” diferentes no cálculo da média ponderada. Os dois primeiros bimestres
possuem peso 2 e os dois últimos peso 3. Sabendo que a média não pode ser representada por
um valor com casas decimais, crie um programa que calcule e apresente a média como um inteiro.
O programa recebe como entrada quatro valores correspondentes as notas de cada unidade."""

# Separando as variáveis de nota
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))

# Separando as variáveis de peso
peso_dois = 2
peso_tres = 3

# Calculo da média das notas

media_das_notas = ((nota1 * 2) + (nota2 * 2) + (nota3 * 3) + (nota4 * 3)) // 10 # O calculo é feito multiplicando a nota pelo peso e dividindo pela soma dos pesos

print(f"Média das notas: {media_das_notas}")