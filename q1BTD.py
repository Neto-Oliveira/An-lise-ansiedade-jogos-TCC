import pandas as pd
from scipy.stats import ttest_rel, f_oneway
from scipy.stats import shapiro
from scipy.stats import wilcoxon

def testar_normalidade(dataframe):
    """
    Testa a normalidade dos dados utilizando o teste de Shapiro-Wilk.

    Parametros:
    - dataframe: DataFrame contendo os dados a serem testados.

    Retorna:
    - Um dicionário onde as chaves são os nomes das colunas e os valores são mensagens indicando se os dados
      seguem uma distribuição normal ou não.
    """
    resultados_normalidade = {}
    alpha = 0.05  # Nível de significância
    
    for coluna in dataframe.columns[1:]:  # Ignorando a coluna 'ID_Jogador'
        stat, p_valor = shapiro(dataframe[coluna])
        if p_valor > alpha:
            resultados_normalidade[coluna] = 'Os dados parecem seguir uma distribuição normal (não rejeitamos H0)'
        else:
            resultados_normalidade[coluna] = 'Os dados não parecem seguir uma distribuição normal (rejeitamos H0)'
    
    return resultados_normalidade

# Dados pré-jogo fornecidos
data_pre_jogo = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10'],
    'Q1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Q2': [0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    'Q3': [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    'Q4': [1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
    'Q5': [2, 0, 2, 0, 0, 0, 0, 0, 1, 0],
    'Q6': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    'Q7': [0, 1, 1, 1, 2, 0, 0, 1, 0, 0],
    'Q8': [0, 1, 2, 0, 1, 0, 0, 0, 0, 0],
    'Q9': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Q10': [0, 1, 1, 2, 2, 1, 1, 1, 0, 0],
    'Q11': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Q12': [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    'Q13': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    'Q14': [1, 0, 3, 0, 1, 0, 0, 0, 0, 0],
    'Q15': [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    'Q16': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    'Q17': [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    'Q18': [0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
    'Q19': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Q20': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Q21': [0, 2, 1, 0, 1, 0, 0, 0, 0, 0]
}


# Dados pós-jogo para os diferentes jogos
data_pos_bloons = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10'],
    'Q1': [0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
    'Q2': [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    'Q3': [0, 1, 0, 1, 0, 2, 0, 1, 0, 0],
    'Q4': [0, 0, 1, 0, 0, 2, 1, 1, 1, 1],
    'Q5': [1, 1, 1, 0, 0, 2, 0, 0, 0, 0],
    'Q6': [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    'Q7': [0, 1, 1, 1, 0, 1, 1, 0, 0, 1],
    'Q8': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    'Q9': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Q10': [0, 1, 0, 1, 0, 2, 0, 1, 0, 1],
    'Q11': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    'Q12': [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    'Q13': [0, 0, 0, 1, 0, 2, 0, 2, 0, 0],
    'Q14': [0, 0, 1, 0, 0, 2, 0, 0, 0, 1],
    'Q15': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    'Q16': [0, 0, 0, 1, 0, 2, 0, 1, 0, 0],
    'Q17': [0, 0, 1, 0, 0, 2, 0, 0, 0, 0],
    'Q18': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Q19': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    'Q20': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Q21': [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]
}

# Convertendo os dicionários em DataFrames do pandas
df_pre_jogo = pd.DataFrame(data_pre_jogo)
df_pos_bloons = pd.DataFrame(data_pos_bloons)



# Aplicando a função na base de dados pré-jogo
resultados_normalidade = testar_normalidade(df_pre_jogo)
resultados_normalidade_cuphead = testar_normalidade(df_pos_bloons)



# Exibindo os resultados
for coluna, resultado in resultados_normalidade.items():
    print(f'{coluna}: {resultado}')
    
for coluna, resultado in resultados_normalidade_cuphead.items():
    print(f'{coluna}: {resultado}')



    
# Calculando média e desvio padrão para cada jogo e cada pergunta
def calcular_stats(dataframe):
    stats_df = dataframe.describe().loc[['mean', 'std']].transpose()
    return stats_df

# Calculando estatísticas descritivas para cada jogo
stats_pre_jogo = calcular_stats(df_pre_jogo)
stats_bloons = calcular_stats(df_pos_bloons)



# Exibindo as estatísticas descritivas
print("Estatísticas descritivas para Pré-jogo:")
print(stats_pre_jogo)
print("Estatísticas descritivas para bloons:")
print(stats_bloons)




# Função para calcular o teste t pareado

def realizar_teste_wilcoxon(df_pre, df_pos):
    """
    Realiza o teste de Wilcoxon pareado para cada variável entre os DataFrames df_pre e df_pos.

    Parâmetros:
    - df_pre: DataFrame contendo os dados pré-jogo.
    - df_pos: DataFrame contendo os dados pós-jogo.

    Retorna:
    - Um DataFrame com os resultados do teste de Wilcoxon para cada variável.
    """
    resultados_wilcoxon = {}
    
    for coluna in df_pre.columns[1:]:  # Ignorando a coluna 'ID_Jogador'
        statistic, p_valor = wilcoxon(df_pre[coluna], df_pos[coluna])
        resultados_wilcoxon[coluna] = {'Estatística do teste': statistic, 'Valor p': p_valor}
    
    return pd.DataFrame(resultados_wilcoxon).transpose()
    
# Calculando teste t pareado para cada jogo
resultado_cuphead = realizar_teste_wilcoxon(df_pre_jogo, df_pos_bloons)



print("Resultado do teste wilcoxon para bloons:")
print(resultado_cuphead)
print("\n")