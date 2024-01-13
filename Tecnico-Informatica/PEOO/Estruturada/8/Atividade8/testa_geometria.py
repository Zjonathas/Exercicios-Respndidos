""""3. Crie um arquivo python para testar as funções presentes no módulo geometria.
Nomeie o arquivo como testa_geometria. O arquivo serve apenas para fazer uso das
funções do módulo criado na questão anterior. Nesse arquivo faça a chamada para
todas as funções do módulo."""

from geometria import *

triangle_false = calculate_perimeter_of_triangle(1, 2, 3)
triangle_true = calculate_perimeter_of_triangle(10, 5, 9)
square = calculate_perimeter_of_square(2, 2 ,2 , 2)
circle = calculate_perimeter_of_circle(4)

print(f"Triângulo um: {triangle_false}\n"
    f"Triângulo dois: {triangle_true}\n"
    f"Quadrado: {square}\n"
    f"Círculo: {circle}")