"""1. Crie um programa com uma função que calcula o preço de um produto após o acréscimo dos
impostos e retorna o valor no formato de moeda (R$ 0.00). A função recebe como parâmetros o
valor do produto, o percentual do imposto estadual que incide sobre o preço do produto e outro
para o imposto federal. O valor do produto sempre precisa ser informado, porém, quando o valor
dos impostos não é informado, a função deve usar os 0,15 como padrão para o imposto estadual
e 0,06 para o imposto federal."""

def add_tax_to_the_price(value, state_percentage = 0.15, federal_percentage = 0.06):
    """ Adiciona os impostos ao preço
    Args:
        value: valor do produto
        state_percentage: percentual do imposto estadual
        federal_percentage: percentual do imposto federal
    Returns:
        valor do produto com os impostos
    """

    federal_tax = value * federal_percentage
    state_tax = value * state_percentage

    amount = value + federal_tax + state_tax

    return f"R$ {amount:.2f}"

print(add_tax_to_the_price(10, 0.1, 0.1))