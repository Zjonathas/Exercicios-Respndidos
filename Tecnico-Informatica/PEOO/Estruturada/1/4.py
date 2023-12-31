""""4. Supondo que não haja acidentes ou atrasos, a distância que um automóvel percorre numa rodovia
pode ser calculada com a seguinte fórmula:

Distância = velocidade × tempo

Sabendo disso, construa um algoritmo em que o usuário possa informar a velocidade em que um
carro está viajando e exiba as seguintes informações:
• A distância que o carro percorrerá em 5 horas;
• A distância que o carro percorre em 8 horas;
• A distância que o carro percorrerá em 12 horas."""

velocidade = float(input("Digite a velocidade do automóvel por hora: "))

distancia_cinco_horas = velocidade * 5
distancia_oito_horas = velocidade * 8
distancia_doze_horas = velocidade * 12

print(f"• A distância que o carro percorrerá em 5 horas; {distancia_cinco_horas:.2f}Km\n"
    f"• A distância que o carro percorre em 8 horas; {distancia_oito_horas:.2f}Km\n"
    f"• A distância que o carro percorrerá em 12 horas. {distancia_doze_horas:.2f}Km\n")
