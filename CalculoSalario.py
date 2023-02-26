from URL_Import import salario_minimo


def hora():
    global horas
    while True:
        # variavel que armazena a informação dada pelo usuario no input
        horas = (input('Quantas horas você trabalhou este mês?'))
        if horas.isdigit():  # verifica se a entrada é um número
            horas = int(horas)  # converte a entrada para int
            break
        else:
            print('Apenas numeros inteiros são permitidos')


hora()


def calcular():
    global calcular
    while True:
        # variavel que recebe o valor de 'salario' e divide pela variavel 'horas'
        salario_hora = salario / horas
        print("O salário mínimo atual é R$ {:.2f}".format(salario_minimo))
        print(f'O valor da sua hora trabalhada é R${salario_hora:.2f}')
        if salario < salario_minimo:
            print('Seu salario esta abaixo do salario minimo.')
            break
        elif salario > salario_minimo:
            print('Seu salario é maior que o salario minimo.')
            break
        else:
            print('Seu salario é igual ao salario minimo')
            break


def salariof():
    global salario
    while True:
        # variavel que armazena a informação dada pelo usuario no input
        salario = input('Qual é o valor do seu salário mensal? ')
        if salario.replace('.', '').isdigit():  # verifica se a entrada é um número
            salario = float(salario)  # converte a entrada para float
            calcular()
            break
        else:
            print('Apenas números são permitidos')


salariof()
