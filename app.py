import pandas as pd
from math import sqrt
import streamlit
import matplotlib.pyplot
import numpy

def ler_arquivo(arquivo):
    return pd.read_csv(arquivo, sep=",")

def desenha_coluna(dataFrame):
    streamlit.title("Análise Estatística de Dados")
    streamlit.subheader("Escolha a coluna para análise e visualize os resultados")

    # Mostreamlitrar DataFrame em expander
    with streamlit.expander("Mostrar Tabela completa"):
        streamlit.dataframe(dataFrame)
 
def separar_coluna(dataFrame):
    desenha_coluna(dataFrame)
    escolha = streamlit.selectbox("Escolha a coluna para análise:", dataFrame.columns)
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
        
def calcular_freq_relativa(classes):
    freqRelativa = []
    
    for inf, sup, freq in classes:
        freqRelativa.append(freq/30)
    return freqRelativa
        
def gerar_info(coluna):
    amplitudeClasses = calcular_amplitude(coluna)
    classes = gerar_classes(coluna, amplitudeClasses) 
    return classes      
    
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

def gerar_histograma(classes):
    larguras = []
    centros = []
    frequencias = []

    for inf, sup, freq in classes:
        centros.append((inf + sup)/2)  # ponto central da classe
        larguras.append(sup - inf)     # largura da barra
        frequencias.append(freq)

    # Criar gráfico
    streamlit.subheader("Histograma de Classes")
    fig, ax = matplotlib.pyplot.subplots()

    # Usar ax.bar com largura personalizada
    ax.bar(centros, frequencias, width=larguras, edgecolor="black", align="center")
    ax.set_xlabel("Intervalos de Classe")
    ax.set_ylabel("Frequência")
    ax.set_title("Histograma de Classes")
    streamlit.pyplot(fig)

def gerar_poligono_frequencia(dados, classes):
    pontosMedios = []
    frequencias = []
    for inf, sup, freq in classes:
        pontosMedios.append((inf+sup)/2)
        frequencias.append(freq)
# Criar gráfico
    streamlit.subheader("Polígono de Frequência")
    fig, ax = matplotlib.pyplot.subplots()

    # Usar ax.bar com largura personalizada
    fig, ax = matplotlib.pyplot.subplots()
    ax.plot(pontosMedios, frequencias, marker="o", linestyle="-", color="b")
    ax.set_xlabel("Classes (pontos médios)")
    ax.set_ylabel("Frequência")
    ax.set_title("Polígono de Frequência")

    streamlit.pyplot(fig)

def gerar_ogiva_galton(dados, classes):
    streamlit.subheader("Ogiva de Galton")
    limeteSuperiores = []
    frequencias = []
    frequenciasAcumuladas = []
    
    for inf, sup, freq in classes:
        limeteSuperiores.append(sup)
        frequencias.append(freq)
    
    frequenciasAcumuladas = numpy.cumsum(frequencias)

    fig, ax = matplotlib.pyplot.subplots()
    ax.plot(limeteSuperiores, frequenciasAcumuladas, marker="o", linestyle="-", color="g")
    ax.set_xlabel("Limite Superior da Classe")
    ax.set_ylabel("Frequência Acumulada")
    ax.set_title("Ogiva de Galton")

    streamlit.pyplot(fig)

def gerar_graficos(dados, classes):

    gerar_histograma(classes)
    gerar_poligono_frequencia(dados, classes)
    gerar_ogiva_galton(dados, classes)

def gerar_classes_grafica(classes):
    df_classes = pd.DataFrame(classes, columns=["Limite Inferior", "Limite Superior", "Frequência"])

    # Mostrar tabela no Streamlit
    streamlit.subheader("Classes de Frequência")
    streamlit.table(df_classes)  # tabela estática 

def gerar_parte_grafica(dados, classes):
    
    gerar_classes_grafica(classes)
    streamlit.header("Estatísticas Calculadas")
    
    # Mostrar estatísticas em colunas
    col1, col2, col3 = streamlit.columns(3)
    
    col1.metric("Média", f"{dados['media']:.2f}")
    col1.metric("Moda", f"{dados['moda']:.2f}")
    
    col2.metric("Mediana", f"{dados['mediana']:.2f}")
    col2.metric("Variância", f"{dados['variancia']:.2f}")
    
    col3.metric("Desvio Padrão", f"{dados['dp']:.2f}")
    col3.metric("Coeficiente de Variabilidade", f"{dados['cv']:.2f}")

    gerar_graficos(dados, classes)

def main():
    dataFrame = ler_arquivo("planilhaValores.csv")
    coluna = separar_coluna(dataFrame)
    classes = gerar_info(coluna)
    dados = gerar_estatisticas(classes)
    gerar_parte_grafica(dados, classes)

if __name__ == "__main__":
    main()