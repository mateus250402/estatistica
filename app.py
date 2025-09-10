import pandas as pd

#Le arquivo e pede coluna
df = pd.read_csv("planilhaValores.csv", sep=",")
print(df.columns)
escolha = input("Qual coluna deseja analisar?")

#pega a coluna , ordena e mostra
coluna = df[escolha].sort_values()
coluna = coluna.reset_index(drop=True)
print(coluna)

