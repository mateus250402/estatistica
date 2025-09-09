# 📊 Guia de Processamento Estatístico
---


## 🗂️ Entradas

- **Arquivo Excel** contendo:
  - **Coluna A:** Valores

---

## ⚙️ Processo

1. **Ler arquivo**
2. **Calcular classess**
    - H = Maior valor - menor valor    
    - K = Raiz de nº elementos aproximado
    - h = K/H
3. **Processar para DataFrame**
   - Classe: tupla `(inf, sup)`
   - Freq: `int`
4. **Calcular estatísticas:**
   - Média:
   - Moda:
   - Mediana:
   - Desvio Padrão:
   - Variância:
   - Coeficiente de Variação (CV):
5. **Gerar gráficos:**
   - Histograma
   - Polígono de frequência
   - Ogiva de Galton

---

## 📤 Saída

- DataFrame com valores de entrada e cálculos individuais
- Lista com valores gerais
- Exibição dos gráficos

---

## 🛠️ Tecnologias

- **Python**
  - Pandas
  - Biblioteca gráfica (ex: Matplotlib, Seaborn)
