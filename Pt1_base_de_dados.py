import pandas as pd

df = pd.read_csv('cancelamentos.csv')
display(df)


df_atualizado = df.drop('CustomerID', axis=1)
display(df_atualizado)

