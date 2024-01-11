""""2. Crie um programa com uma função que recebe uma data no formato dd/mm/aaaa e efetua uma
validação dessa data. Lembre o que uma data precisa para ser um valor válido (quantidade de dias
em um mês, etc). Caso a data seja válida, a função deve retornar a data no formato “dd de
mêsporextenso de aaaa”, exemplo: 01/01/2022 após ser validada e formatada é retornada como
01 de janeiro de 2022. A formatação da data deve ficar a cargo de uma outra função que faz
apenas essa tarefa."""

def format_date(date):
    months = ['Janeiro', 'Fevereiro','Março',
              'Abril','Maio','Junho','Julho',
              'Agosto','Setembro','Outubro','Novembro','Dezembro',]

    month = months[int(date[3:5]) - 1]

    formated_date = f'{date[0:2]} de {month} de {date[6:]}'
    return formated_date

def validate_the_date(date:str):
    if int(date[0:2]) > 31 or int(date[0:2]) < 1:
        return 'Data inválida!'
    elif int(date[3:5]) > 12 or int(date[3:5]) < 1:
        return 'Data inválida!'
    elif int(date[6:]) > 2024 or int(date[3:5]) < 1:
        return 'Data inválida!'

    return format_date(date)

print(validate_the_date('02/03/2022'))

