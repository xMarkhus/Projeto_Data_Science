from Pt2_tratar_erros import df_tratado

# verificando a taxa de cancelamento
display(df_tratado['cancelou'].value_counts(normalize=True).map('{:.1%}'.format))

# taxa de cancelamento se encontra em 56.7%


# verificando a taxa de cancelamento por tipo de assintura
display(df_tratado[['duracao_contrato', 'cancelou']].groupby('duracao_contrato').mean())

# primeiro problema detectado, 100% dos contratos mensais são cancelados

# Analisando as estatísticas de cancelamento sem o plano mensal
df_filtrado = df_tratado[df_tratado['duracao_contrato'] != 'Monthly']

display(df_filtrado['cancelou'].value_counts(normalize=True).map('{:.1%}'.format))

# A taxa de cancelamento cai de 56.7% para 46.1%

