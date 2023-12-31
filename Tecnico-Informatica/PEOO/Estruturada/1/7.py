"""7. Ajustador de receitas – Uma receita de biscoitos para produzir 48 unidades exige a seguinte
quantidade de ingredientes:
a) 1,5 xícaras de açúcar
b) 1 xícara de manteiga
c) 2,75 xícaras de farinha
d) 3 ovos
Crie um algoritmo que pergunte ao usuário quantos cookies ele deseja fazer e calcule a quantidade
correspondente dos ingredientes. Exemplo: as quantidades listadas servem para fazer 48
unidades. Se o usuário quisesse produzir 96 unidades (ou seja, o dobro de 48) as quantidades dos
ingredientes devem ser dobradas: 3 xícaras de açúcar, 2 xícaras de manteiga, 5,5 xícaras de farinha
e 6 ovos. Do mesmo modo, se a quantidade de biscoitos for menor que 48, o algoritmo também
deve fazer o ajuste."""

quantidade_de_biscoitos = int(input("Digite a quantidede de biscoitos: "))

quantidade_de_xicaras_de_acucar = quantidade_de_biscoitos * 1.5 / 48
quantidade_de_xicaras_de_manteiga = quantidade_de_biscoitos * 1 / 48
quantidade_de_xicaras_de_farinha = quantidade_de_biscoitos * 2.75 / 48
quantidade_de_ovos = quantidade_de_biscoitos * 3 / 48

print(f"Xícaras de açúcar necessárias: {quantidade_de_xicaras_de_acucar:.2f}\n"
      f"Xícaras de manteiga necessárias: {quantidade_de_xicaras_de_manteiga:.2f}\n"
      f"Xícaras de farinha necessárias: {quantidade_de_xicaras_de_farinha:.2f}\n"
      f"Ovos necessários: {quantidade_de_ovos:.2f}\n")