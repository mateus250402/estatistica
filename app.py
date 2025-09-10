import pandas as pd
from math import sqrt

def ler_arquivo(arquivo):
    return pd.read_csv(arquivo, sep=",")

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
      
def calcular_media(classes):
    somaXi = totalFreq = 0
    for inf, sup, freq in classes:
        somaXi += ((inf+sup)/2)*freq
        totalFreq += freq
    media = somaXi/totalFreq
    
    return media
   
def calcular_moda(classes):
    classeModal = max(classes, key=lambda x: x[2])
    infModal, supModal, freqModal = classeModal
    indiceModal = classes.index(classeModal)
    
    freqAnt = classes[indiceModal - 1][2] if indiceModal > 0 else 0
    freqProx = classes[indiceModal + 1][2] if indiceModal < len(classes) - 1 else 0
    h = supModal - infModal
    
    dividendo = freqModal - freqAnt
    divisor = dividendo + (freqModal - freqProx)
    moda = infModal + (dividendo/divisor)*h
    
    return moda

def calcular_mediana(classes):
    N = 0
    for inf, sup, freq in classes:
        N += freq
    
    posicaoMediana = N / 2
    
    freqAcumulada = 0
    for i, (inf, sup, freq) in enumerate(classes):
        freqAcumulada += freq
        if freqAcumulada >= posicaoMediana:
            infMediana = inf
            supMediana = sup
            freqMeidana = freq
            freqAnt = freqAcumulada - freqMeidana
            h = supMediana - infMediana
            break
        
    mediana = infMediana + ((posicaoMediana - freqAnt)/freqMeidana)*h
    
    return mediana
        
def calcular_variancia(classes, media):
    soma = 0

    for inf, sup, freq in classes:
        xi = sup - inf
        soma += freq*(xi - media) ** 2
    variancia = soma / len(classes)
    
    return variancia

def calcular_dp(variancia):
    dp = sqrt(variancia)
    
    return dp

def calcular_cv(dp, media):
    cv = dp / media
    
    return cv
        
def gerar_classes(arquivo):
    dataFrame = ler_arquivo(arquivo)
    coluna = separar_coluna(dataFrame)
    amplitudeClasses = calcular_amplitude(coluna)
    classes = gerar_classes(coluna, amplitudeClasses)       

def gerar_estatisticas(classes):
    media = calcular_media(classes)
    moda = calcular_moda(classes)
    mediana = calcular_mediana(classes)
    variancia = calcular_variancia(classes, media)
    desvioPadrao = calcular_dp(variancia)
    coeficienteVariabilidade = calcular_cv(desvioPadrao, media)
    
    dados = {
        "media" : media,
        "moda" : moda,
        "mediana" : mediana,
        "variancia" : variancia,
        "dp" : desvioPadrao,
        "cv" : coeficienteVariabilidade
    }
    
    return dados

def main():
    classes = gerar_classes("planilhaValores.csv")
    dados = gerar_estatisticas(classes)

if __name__ == "__main__":
    main()