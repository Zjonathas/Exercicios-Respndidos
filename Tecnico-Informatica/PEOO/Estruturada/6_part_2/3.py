"""3. Crie um programa com uma única função que calcula a área de três formas geométricas: triângulo,
círculo e trapézio. A função deve receber obrigatoriamente um parâmetro que indica a forma que
terá sua área calculada (exemplo: 1 para triângulo, 2 para círculo e 3 para trapézio). Os demais
parâmetros dependem de como é calculada a área da forma geométrica. A função deve retornar
o resultado do cálculo da área. As fórmulas para o cálculo das áreas estão listadas abaixo:
    - Triângulo: base * altura / 2
    - Círculo: pi * raio^2
    - Trapézio: (Base maior + base menor) / 2 * altura"""

def calculate_area(form, **kwargs):
    PI = 3.14
    if form == '1':
        return kwargs['base'] * kwargs['altura'] / 2
    elif form == '2':
        return PI * kwargs['raio'] ** 2
    return (kwargs['base_maior'] + kwargs['base_menor']) / 2 * kwargs['altura']

while True:
    choice = input('1 para triângulo | 2 para círculo | 3 para trapézio | 0 para sair: ')
    match choice:
        case '1':
            base = float(input('Digite a base do triângulo: '))
            height = float(input('Digite a altura do triângulo: '))
            area  = calculate_area(choice, base=base, altura=height)
            
            print(f'A área do triângulo é: {area:.2f}')
        case '2':
            radius = float(input('Digite o raio do círculo: '))
            area  = calculate_area(choice, raio = radius)
            
            print(f'A área do círculo é: {area:.2f}')
        case '3':
            smallest_base = float(input('Digite a base menor do trapézio: '))
            largest_base = float(input('Digite a base maior do trapézio: '))
            height = float(input('Digite a altura do trapézio: '))
            area  = calculate_area(choice,
                base_maior = largest_base,
                base_menor = smallest_base,
                altura = height)
            
            print(f'A área do trapézio é: {area:.2f}')
        case '0':
            break
        case _:
            print('Opção inválida!')