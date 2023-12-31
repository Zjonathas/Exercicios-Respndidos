"""2. Crie um programa que simula um radar de velocidade. O programa recebe a velocidade do veículo
e, caso ela seja superior a 80 km, o programa informa que o condutor foi multado e o valor da
multa. O valor da multa é de 50 reais para cada quilômetro a mais que o limite permitido."""

velocidade_do_veiculo = float(input("Digite a velocidade do veículo: "))

if velocidade_do_veiculo > 80:
    valor_da_multa = (velocidade_do_veiculo - 80) * 50
    print(f"O condutor foi multado em R$ {valor_da_multa:.2f}")
else:
    print("Tudo okay")
