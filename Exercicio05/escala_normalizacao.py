# Exercício 5 — Influência da escala e normalização
# Atributos: Idade e Renda (R$).

import math
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 22. Criando o DataFrame com pandas
dados = {
    "Cliente": ["A", "B", "C", "D", "E"],
    "Idade": [20, 25, 40, 55, 70],
    "Renda": [2000, 3000, 6000, 9000, 12000],
}
df = pd.DataFrame(dados).set_index("Cliente")

print("Dados originais:")
print(df)

# 23. Distância Euclidiana entre A e B com os valores originais
distancia_original = math.dist(df.loc["A"], df.loc["B"])
print(f"\nDistância A-B com valores originais: {distancia_original:.2f}")

# 24. Normalizando Idade e Renda com MinMaxScaler
scaler = MinMaxScaler()
df_normalizado = pd.DataFrame(
    scaler.fit_transform(df[["Idade", "Renda"]]),
    columns=["Idade", "Renda"],
    index=df.index,
)

# 25. Exibindo o DataFrame normalizado
print("\nDados normalizados (MinMaxScaler):")
print(df_normalizado)

# 26. Calculando novamente a distância entre A e B com os valores normalizados
distancia_normalizada = math.dist(
    df_normalizado.loc["A"], df_normalizado.loc["B"]
)
print(f"\nDistância A-B com valores normalizados: {distancia_normalizada:.4f}")

# 27. Comparando os dois resultados
print("\nComparação:")
print(f"  Distância original:     {distancia_original:.2f}")
print(f"  Distância normalizada:  {distancia_normalizada:.4f}")

# Por que a renda domina a distância nos valores originais?
# Na distância Euclidiana cada atributo entra com seu valor absoluto. A renda
# varia na casa dos milhares (2000 a 12000), enquanto a idade varia na casa das
# dezenas (20 a 70). Assim, a diferença de renda entre A e B (1000) é muito
# maior que a diferença de idade (5), e o termo da renda ao quadrado domina
# completamente o cálculo. Após a normalização MinMax, ambas as colunas passam
# a variar entre 0 e 1, colocando os atributos na mesma escala e permitindo que
# cada um contribua de forma equilibrada para a distância.
