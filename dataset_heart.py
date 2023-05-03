import pandas as pd

coracao = pd.read_csv('heart.csv')

print('CONJUNTO DE DADOS EM UM DATAFRAME')
print(coracao)
print('----------//------------//--------------')

print('PRIMEIRAS LINHAS DO DATAFRAME USANDO .head()')
print(coracao.head(10))

print('----------//------------//--------------')

print('ÚLTIMAS LINHAS DO DATAFRAME')
print(coracao.tail(10))

print('----------//------------//--------------')

print('DIMENSÕES DO DATAFRAME')
print(coracao.shape)

print('-----------------------//-----------------------//---------------------------')
print('OBTENDO INFORMAÇÕES SOBRE AS COLUNAS DO DATAFRAME')

print(coracao.info())

print('--------------------------//------------------------//-----------------')
print('ESTATÍSTICAS DESCRITIVAS BÁSICAS DO DATAFRAME')

print(coracao.describe())

print('------------------//--------------------//----------------------')

print('SELECIONANDO COLUNAS ESPECÍFICAS(as 20 primeiras linhas)')

col_específicas = ['age','sex','oldpeak']
print((coracao[col_específicas]).head(20))

print('--------------------//----------------------//-------------------------')

print('SELECIONANDO LINHAS ESPECÍFICAS DE UM DATAFRAME USANDO O MÉTODO loc[] // AQUI SELECIONEI LINHAS ONDE A IDADE(age) É MAIOR QUE 50 ANOS.')

print(coracao.loc[coracao['age'] >= 50])

print('--------------------//----------------------//-------------------------')

print("FILTRANDO LINHAS DO DATAFRAME COM BASE EM UMA CONDIÇÃO USANDO OS OPERADORES LÓGICOS '&' E '|' ")

condicao_e = (coracao['age'] >= 50) & (coracao['sex'] == 1)

filtro_condicao_e = coracao.loc[condicao_e]

print(filtro_condicao_e)
print(condicao_e)

print("AGORA USAREMOS O OPERADOR '|' ")

condicao_ou = (coracao['trestbps'] > 130) | (coracao['oldpeak'] < 0.3)

filtro_condicao_ou = coracao.loc[condicao_ou]

print(filtro_condicao_ou)
print(condicao_ou)

print((coracao.loc[condicao_ou]).head(10))

print('---------------------//---------------------//--------------------')

print('USANDO O MÉTODO groupby() VOU AGRUPAR A COLUNA "sex" E DESCOBRIR QUAL A MÉDIA DE IDADES DE ACORDO COM CADA SEXO(1 = MASCULUNO, 0 = FEMININO)')

agrupando = coracao.groupby('sex')

print((agrupando['age'].mean()).round(2))

print('-----------------//-------------------//------------------')

print('ORDENANDO O DATAFRAME USANDO O MÉTODO sort_values(), PARA QUE A COLUNA age(IDADE) seja exibida de forma DECRESCENTE')

cres_desc = coracao.sort_values(by='age', ascending=False)

print(cres_desc)









