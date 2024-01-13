"""2. Dentro do pacote crie um módulo chamado geometria e defina funções para calcular
o perímetro de três formas geométricas: o triângulo, o quadrado e o círculo.
    • OBS1: pesquise na internet como se calcula o perímetro dessas formas
    • OBS2: use a constante pi do módulo math
    • OBS3: para ser considerado um triângulo, é necessário verificar os valores dos
seus lados usando uma regra de condição de existência. Pesquise sobre essa
regra e implemente uma função para fazer essa verificação antes de proceder
com o cálculo do perímetro. Ou seja, só pode calcular o perímetro do triângulo
se ele tiver sido validado como um triângulo."""

from math import fabs, pi

def validate_triangle(side_a, side_b, side_c):
    """
    Parâmetros:
        side_a: lado a do triângulo
        side_b: lado b do triângulo
        side_c: lado c do triângulo

    Retorna:
        True se os lados formam um triângulo, False caso contrário.
    """
    operation_a = fabs(side_a + side_b)
    operation_b = fabs(side_a + side_c)
    operation_c = fabs(side_c + side_b)

    if operation_a <= side_c or operation_b <= side_b or operation_c <= side_a: 
        return False
    
    return True


def calculate_perimeter_of_triangle(side_a, side_b, side_c):
    if validate_triangle(side_a, side_b, side_c):
        perimeter = side_a + side_b + side_c
        return perimeter
    
    return 'Triângulo inválido!'

def calculate_perimeter_of_square(side_one, side_two, side_three, side_four):
    return side_one + side_two + side_three + side_four

def calculate_perimeter_of_circle(radius):
    return 2 * pi * radius



if __name__ == '__main__':
    triangle_false = calculate_perimeter_of_triangle(1, 2, 3)
    triangle_true = calculate_perimeter_of_triangle(10, 5, 9)
    square = calculate_perimeter_of_square(2, 2 ,2 , 2)
    circle = calculate_perimeter_of_circle(4)

    print(f"Triângulo um: {triangle_false}\n"
        f"Triângulo dois: {triangle_true}\n"
        f"Quadrado: {square}\n"
        f"Círculo: {circle}")