# Funções (parte 2)

1. Crie um programa com uma função que calcula o preço de um produto após o acréscimo dos
impostos e retorna o valor no formato de moeda (R$ 0.00). A função recebe como parâmetros o
valor do produto, o percentual do imposto estadual que incide sobre o preço do produto e outro
para o imposto federal. O valor do produto sempre precisa ser informado, porém, quando o valor
dos impostos não é informado, a função deve usar os 0,15 como padrão para o imposto estadual
e 0,06 para o imposto federal.

2. Crie um programa com uma função que recebe uma data no formato dd/mm/aaaa e efetua uma
validação dessa data. Lembre o que uma data precisa para ser um valor válido (quantidade de dias
em um mês, etc). Caso a data seja válida, a função deve retornar a data no formato “dd de
mêsporextenso de aaaa”, exemplo: 01/01/2022 após ser validada e formatada é retornada como
01 de janeiro de 2022. A formatação da data deve ficar a cargo de uma outra função que faz
apenas essa tarefa.

3. Crie um programa com uma única função que calcula a área de três formas geométricas: triângulo,
círculo e trapézio. A função deve receber obrigatoriamente um parâmetro que indica a forma que
terá sua área calculada (exemplo: 1 para triângulo, 2 para círculo e 3 para trapézio). Os demais
parâmetros dependem de como é calculada a área da forma geométrica. A função deve retornar
o resultado do cálculo da área. As fórmulas para o cálculo das áreas estão listadas abaixo:
    - Triângulo: base * altura / 2
    - Círculo: pi * raio2
    - Trapézio: (Base maior + base menor) / 2 * altura