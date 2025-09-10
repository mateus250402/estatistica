import pandas as pd
from math import sqrt

def ler_arquivo():
    return pd.read_csv("planilhaValores.csv", sep=",")

def separar_coluna(dataFrame):
    print(dataFrame.columns)
    
    escolha = input("Qual coluna deseja analisar? ")
    coluna = dataFrame[escolha].sort_values()
    coluna = coluna.reset_index(drop=True)
    
    return coluna

def calcular_amplitude(coluna):
    maiorValor = coluna.max()
    menorValor = coluna.min()
    
    amplitudeTotal = maiorValor - menorValor
    K = sqrt(len(coluna))  # Raiz quadrada do número de elementos
    amplitudeClasses = round(amplitudeTotal / K)
    
    return amplitudeClasses

def gerar_classes(coluna, amplitudeClasses):
    maiorValor = coluna.max()
    menorValor = coluna.min()
    
    classes = []
    
    limInf = menorValor
    while limInf < maiorValor:
        limSup = limInf + amplitudeClasses     
        freq =  len(coluna[(coluna >= limInf) & (coluna < limSup)])     
        classes.append((int(limInf), int(limSup), freq))
        limInf = limSup
        
    return classes
             

def main():
    dataFrame = ler_arquivo()
    coluna = separar_coluna(dataFrame)
    amplitudeClasses = calcular_amplitude(coluna)
    classes = gerar_classes(coluna, amplitudeClasses)
    print(classes)
    

if __name__ == "__main__":
    main()