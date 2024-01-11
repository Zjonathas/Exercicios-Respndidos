"""2. Crie um programa que efetue a conversão de temperaturas de Célsius para Farenheit e o contrário
também, de Farenheit para Célsius. O programa deve perguntar qual das duas conversões o
usuário deseja realizar e só depois receber a temperatura. Ao final, o programa precisa exibir o
valor digitado pelo usuário e a temperatura convertida. Use quantas funções considerar
necessário. Considere as fórmulas de conversão abaixo:
    - De graus Celsius (C) para graus Fahrenheit (F): F = 1,8C + 32
    - De graus Fahrenheit (F) para graus Celsius (C): C = (F – 32)/1,8"""


def fahrenheit_to_celcius(value):
    return (value - 32) / 1.8

def celsius_to_fahrenheit(value):
    return 1.8 * value + 32

while True:
    choice = input('Qual conversão você deseja realizar? F = Fahrenheit | C = Celsius: ').upper()
    
    if choice == 'F':
        fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
        celsius = fahrenheit_to_celcius(fahrenheit)
        print(f'Conversão feita com sucesso!\n'
              f'Celsius: {celsius}\n'
              f'Fahrenheit: {fahrenheit}')
        break
    elif choice == 'C':
        celsius = float(input('Digite a temperatura em Celsius: '))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f'Conversão feita com sucesso!\n'
              f'Celsius: {celsius}\n'
              f'Fahrenheit: {fahrenheit}')
        break
    else:
        print('Opção inválida, tente novamente!')