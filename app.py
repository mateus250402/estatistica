import pandas

#Le arquivo e pede coluna
dataFrame = pandas.read_csv("planilhaValores.csv", sep=",")
print(dataFrame.columns)
escolha = input("Qual coluna deseja analisar?")

#pega a coluna , ordena e mostra
coluna = dataFrame[escolha].sort_values()
coluna = coluna.reset_index(drop=True)
print(coluna)

