import pandas as pd

car = pd.read_csv('carros.csv', sep=';')

print(car.head(5))

print('------------------------//------------------------//-------------------//--------------')

print('TIPOS DE DADOS DO DATASET')
print(car.dtypes)
print('')
print('Os tipos de dados das colunas são: STRING, FLOAT, INTEIRO E BOOLEANO')

print('--------------------//--------------------//------------------//-----------------')

print('DESCRIBE DAS COLUNAS ESPECÍFICAS QUILOMETRAGEM E VALOR')

describe_colunas = ['Quilometragem', 'Valor']

colunas_selecionadas = car[describe_colunas]

descricao = (colunas_selecionadas.describe()).round(0)


print(descricao)

print('')
print('O QUE ESSES VALORES SIGNIFICAM?')
print("""
count: número de valores não nulos na coluna
mean: média dos valores na coluna.
std: desvio padrão dos valores na coluna, que mede a dispersão dos dados.
min: valor mínimo presente na coluna.
25%: primeiro quartil dos dados, também conhecido como quartil inferior ou percentil 25.
50%: segundo quartil dos dados, também conhecido como mediana ou percentil 50. Representa o valor que divide a distribuição em duas partes iguais.
75%: terceiro quartil dos dados, também conhecido como quartil superior ou percentil 75.
max: valor máximo presente na coluna.""")

print('----------//------------------//------------------------')
print('')
print('MAIS INFORMAÇÕES DO DATASET COM A FUNÇÃO INFO().')
print(car.info())

