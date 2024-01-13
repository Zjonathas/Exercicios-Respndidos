"""1. Crie um programa que simula uma agenda de contatos. Os contatos possuem apenas
nome, e-mail e telefone. O programa deve permitir ao usuário cadastrar um novo
contato ou listar os contatos existentes. Essas ações devem estar inseridas em funções.
A aplicação deve permanecer em execução até que o usuário informe que não deseja
mais realizar nenhuma operação.
OBS1: a operação de listar os contatos deve exibir cada contato no formato abaixo:
Nome: nome do contato
E-mail: email do contato
Telefone: telefone do contato
OBS2: lembre que quando há a tentativa de abertura de um arquivo no modo de
leitura, ocorre um erro quando ele não existe."""

def register_contact(name, email, phone):
    with open('contatos.txt', 'a', encoding='utf-8') as data:
        data.write(f'{name} | ')
        data.write(f'{email} | ')
        data.write(f'{phone} |')


def list_cotacts():
    print('-' * 50)
    with open('contatos.txt', 'r', encoding='utf-8') as data:
        for linha in data:
            print(linha, end='')
    print()  # apenas para quebrar linh
    print('-' * 50)
    print()  # apenas para quebrar linh


while True:
    choice = input('1 - Adicionar contato | 2 - Listar contatos | 0 - Sair: ')
    match choice:
        case '1':
            nome = input('Digite o nome: ')
            email = input('Digite o email: ')
            phone = input('Digite o telefone: ')
            register_contact(nome, email, phone)
            print('Sucesso!')
        case '2':
            list_cotacts()
        case '0':
            break
