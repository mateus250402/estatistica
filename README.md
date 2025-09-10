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
   - Média: $\bar{x} = \frac{\sum_{i=1}^{n} \frac{inf_i + sup_i}{2} \cdot f_i}{\sum_{i=1}^{n} f_i}$

   - Moda: $Mo = inf_{mo}+\frac{(f_{mo} - f_{mo-1})}{(f_{mo} - f_{mo-1})+(f_{mo} - f_{mo+1})}*h$

   - Mediana:
      - $N = \frac{\sum_{i=1}^{n} f_i}{2}$
      - L = inferior da classe mediana
      - $F_{ant} = \sum_{i=1}^{me-1} f_i$

      $Mediana = inf + \frac{N - F_{ant}}{F_m}*h$

   - Variância: 
      - N para população, N - 1 para amostar
   
      $s^2 = \frac{\sum_{i=1}^{n} f_i*(x_i-\bar{x})^2}{N}$

   - Desvio Padrão: $\sqrt{s^2}$

   - Coeficiente de Variação (CV): $CV = \frac{DP}{\bar{x}}* 100\%$

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
