from Pt1_base_de_dados import df_atualizado

# verificando se há valores vazios
display(df_atualizado.info())

# excluindo linhas com valores vazios
df_tratado = df_atualizado.dropna()
display(df_tratado.info())

