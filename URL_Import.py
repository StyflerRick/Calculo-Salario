import requests
import re

# Faz a requisição HTTP para a página que contém o valor atual do salário mínimo
url = 'https://www.google.com/search?client=opera-gx&q=salario+minimo+atualmente&sourceid=opera&ie=UTF-8&oe=UTF-8'
try:
    response = requests.get(url)
    response.raise_for_status()  # Verifica se a requisição foi bem sucedida
except requests.exceptions.RequestException as e:
    print(f'Erro ao fazer requisição HTTP: {e}')
    exit()

# Extrai o valor do salário mínimo da resposta HTTP usando uma expressão regular
salario_minimo_str = re.search(r"R\$\s*(\d+\.\d+,\d+)", response.text)
if salario_minimo_str:
    salario_minimo_str = salario_minimo_str.group(1).replace('.', '').replace(
        ',', '.')  # Converte para um formato de ponto flutuante
    salario_minimo = float(salario_minimo_str)
else:
    print('Não foi possível obter o valor do salário mínimo')
