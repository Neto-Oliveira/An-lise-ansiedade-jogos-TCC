import pandas as pd
from scipy.stats import ttest_rel, f_oneway, wilcoxon, shapiro


# Dados da frequencia cardiaca pré-jogo e pós-jogo para cada jogo
data_pre_jogo_bloons  = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10'],
    'fq': [80,73,90,69,87,63,65,83,87,83]
}

data_pos_jogo_bloons  = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10'],
    'fq': [65,70,78,77,79,72,87,71,75,85]
}

# Convertendo os dicionários em DataFrames do pandas
df_pre_jogo_bloons  = pd.DataFrame(data_pre_jogo_bloons )
df_pos_jogo_bloons  = pd.DataFrame(data_pos_jogo_bloons )

# Calculando média e desvio padrão do pré/pós jogo para cada frequência
def calcular_stats(dataframe):
    stats_df = dataframe.describe().loc[['mean', 'std']].transpose()
    return stats_df

# Calculando estatísticas descritivas para pré/pós jogo
stats_pre_jogo_bloons  = calcular_stats(df_pre_jogo_bloons )
stats_pos_jogo_bloons  = calcular_stats(df_pos_jogo_bloons )

# Exibindo as estatísticas descritivas
print("Estatísticas descritivas para Pré-bloons :")
print(stats_pre_jogo_bloons )
print("Estatísticas descritivas para Pós-bloons :")
print(stats_pos_jogo_bloons )

# Função para calcular o teste de Shapiro-Wilk para normalidade
def calcular_teste_normalidade(dataframe):
    resultados_normalidade = {}
    for coluna in dataframe.columns[1:]:  # Começa da segunda coluna para evitar 'ID_Jogador'
        stat, p_valor = shapiro(dataframe[coluna])
        resultados_normalidade[coluna] = {'W-statistic': stat, 'p_valor': p_valor}
    return pd.DataFrame(resultados_normalidade).transpose()

# Calculando teste de normalidade para cada jogo
resultado_normalidade_pre_bloons  = calcular_teste_normalidade(df_pre_jogo_bloons )
resultado_normalidade_pos_bloons  = calcular_teste_normalidade(df_pos_jogo_bloons )

print("Resultado do teste de normalidade para Pré-bloons :")
print(resultado_normalidade_pre_bloons )
print("\n")

print("Resultado do teste de normalidade para Pós-bloons :")
print(resultado_normalidade_pos_bloons )
print("\n")

# Função para calcular o teste de Wilcoxon pareado
def calcular_teste_wilcoxon_pareado(df_pre, df_pos):
    resultados_wilcoxon_pareado = {}
    for coluna in df_pre.columns[1:]:  # Começa da segunda coluna para evitar 'ID_Jogador'
        stat, p_valor = wilcoxon(df_pre[coluna], df_pos[coluna])
        resultados_wilcoxon_pareado[coluna] = {'W-statistic': stat, 'p_valor': p_valor}
    return pd.DataFrame(resultados_wilcoxon_pareado).transpose()

# Calculando teste de Wilcoxon pareado para cada jogo
resultado_wilcoxon_bloons  = calcular_teste_wilcoxon_pareado(df_pre_jogo_bloons , df_pos_jogo_bloons )

print("Resultado do teste de Wilcoxon pareado para Cuphead:")
print(resultado_wilcoxon_bloons)
print("\n")
