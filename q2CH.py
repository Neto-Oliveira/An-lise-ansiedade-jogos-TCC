import pandas as pd
from scipy.stats import ttest_rel, f_oneway, wilcoxon, shapiro


# Dados da frequencia cardiaca pré-jogo e pós-jogo para cada jogo
data_pre_jogo_cuphead  = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'],
    'fq': [78,57,79,77,81,80,74,76,71,72,82,83,74,86,69,79,75,81,57,76,89]
}

data_pos_jogo_cuphead = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'],
    'fq': [82,84,89,82,82,106,69,87,84,80,87,73,83,85,74,70,87,78,67,89,87]
}

# Convertendo os dicionários em DataFrames do pandas
df_pre_jogo_cuphead = pd.DataFrame(data_pre_jogo_cuphead)
df_pos_jogo_cuphead = pd.DataFrame(data_pos_jogo_cuphead)

# Calculando média e desvio padrão do pré/pós jogo para cada frequência
def calcular_stats(dataframe):
    stats_df = dataframe.describe().loc[['mean', 'std']].transpose()
    return stats_df

# Calculando estatísticas descritivas para pré/pós jogo
stats_pre_jogo_cuphead = calcular_stats(df_pre_jogo_cuphead)
stats_pos_jogo_cuphead = calcular_stats(df_pos_jogo_cuphead)

# Exibindo as estatísticas descritivas
print("Estatísticas descritivas para Pré-Cuphead:")
print(stats_pre_jogo_cuphead)
print("Estatísticas descritivas para Pós-Cuphead:")
print(stats_pos_jogo_cuphead)

# Função para calcular o teste de Shapiro-Wilk para normalidade
def calcular_teste_normalidade(dataframe):
    resultados_normalidade = {}
    for coluna in dataframe.columns[1:]:  # Começa da segunda coluna para evitar 'ID_Jogador'
        stat, p_valor = shapiro(dataframe[coluna])
        resultados_normalidade[coluna] = {'W-statistic': stat, 'p_valor': p_valor}
    return pd.DataFrame(resultados_normalidade).transpose()

# Calculando teste de normalidade para cada jogo
resultado_normalidade_pre_cuphead = calcular_teste_normalidade(df_pre_jogo_cuphead)
resultado_normalidade_pos_cuphead = calcular_teste_normalidade(df_pos_jogo_cuphead)

print("Resultado do teste de normalidade para Pré-Cuphead:")
print(resultado_normalidade_pre_cuphead)
print("\n")

print("Resultado do teste de normalidade para Pós-Cuphead:")
print(resultado_normalidade_pos_cuphead)
print("\n")

# Função para calcular o teste de Wilcoxon pareado
def calcular_teste_wilcoxon_pareado(df_pre, df_pos):
    resultados_wilcoxon_pareado = {}
    for coluna in df_pre.columns[1:]:  # Começa da segunda coluna para evitar 'ID_Jogador'
        stat, p_valor = wilcoxon(df_pre[coluna], df_pos[coluna])
        resultados_wilcoxon_pareado[coluna] = {'W-statistic': stat, 'p_valor': p_valor}
    return pd.DataFrame(resultados_wilcoxon_pareado).transpose()

# Calculando teste de Wilcoxon pareado para cada jogo
resultado_wilcoxon_cuphead = calcular_teste_wilcoxon_pareado(df_pre_jogo_cuphead, df_pos_jogo_cuphead)

print("Resultado do teste de Wilcoxon pareado para Cuphead:")
print(resultado_wilcoxon_cuphead)
print("\n")
