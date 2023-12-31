"""5. Nos EUA, a unidade de distância é a milha e unidade de volume para abastecimento de um
automóvel é o galão. Assim, o valor do consumo em milhas por galão (MPG) de um automóvel
pode ser calculado com a seguinte fórmula:
MPG = Número de milhas percorridas / Número de galões de gasolina consumidos
A partir dessas informações, crie um algoritmo que solicite ao usuário a distância percorrida pelo
automóvel em milhas, quantos galões de gasolina foram consumidos para percorrer essa distância
e calcule o consumo em milhas por galão. Considerando que no Brasil usamos quilômetros e
litros invés de milhas e galões, seu programa deve exibir na tela, além do valor em milhas por
galão, o valor do consumo em quilômetros por litro. Para fazer a conversão entre as unidades de
medida, leve em consideração que um galão contém cerca de 3,78 litros e uma milha equivale a
1,61 quilômetros."""

distancia_percorrida = float(input("Digite a distância percorrida em milhas: "))
galoes_consumidos = float(input("Digite a quantidade de galões de gasolina consumidos: "))

volume_galao = 3.78
milha = 1.61

numero_de_milhas_por_galao = distancia_percorrida / galoes_consumidos

km_percorrido = distancia_percorrida * milha

numero_de_km_percorridos_por_litro = km_percorrido * (volume_galao * galoes_consumidos)

print(f"Milhas por galão: {numero_de_milhas_por_galao:.2f}\n"
      f"Km por litro: {numero_de_km_percorridos_por_litro:.2f}\n")