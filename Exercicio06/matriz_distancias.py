# Exercício 6 — Matriz de distâncias entre registros

import math
from itertools import combinations

import pandas as pd

registros = {
    "A": [1, 1],
    "B": [4, 5],
    "C": [2, 2],
    "D": [5, 4],
}

nomes = list(registros.keys())

# 28. Calculando a distância Euclidiana entre todos os pares de registros
distancias = {}
for nome1, nome2 in combinations(nomes, 2):
    distancias[(nome1, nome2)] = math.dist(registros[nome1], registros[nome2])

# 29. Construindo a matriz de distâncias com pandas.DataFrame
matriz = pd.DataFrame(0.0, index=nomes, columns=nomes)

for (nome1, nome2), distancia in distancias.items():
    matriz.loc[nome1, nome2] = distancia
    matriz.loc[nome2, nome1] = distancia  # matriz simétrica

print("Matriz de distâncias:")
print(matriz.round(2))

# 30. Identificando o menor valor diferente de zero
pares = {
    par: valor for par, valor in distancias.items() if valor != 0
}
par_mais_proximo = min(pares, key=pares.get)
menor_distancia = pares[par_mais_proximo]

# 31. Informando o par de registros mais próximo
print(
    f"\nPar mais próximo: {par_mais_proximo[0]} e {par_mais_proximo[1]} "
    f"(distância {menor_distancia:.2f})"
)

# 32. Verificando que a diagonal principal possui apenas zeros
diagonal_zerada = all(matriz.loc[nome, nome] == 0 for nome in nomes)
print(f"Diagonal principal contém apenas zeros: {diagonal_zerada}")

# 33. Verificando que a matriz é simétrica
simetrica = matriz.equals(matriz.T)
print(f"Matriz é simétrica: {simetrica}")

# Por que a diagonal é zero?
# A diagonal representa a distância de cada registro para ele mesmo. Como não
# há diferença em nenhum atributo, a soma dos quadrados é zero e a raiz também.
#
# Por que d(A, B) = d(B, A)?
# Cada termo da distância Euclidiana usa (a_i - b_i) elevado ao quadrado, e
# (a_i - b_i)^2 = (b_i - a_i)^2. A soma e a raiz são, portanto, idênticas nas
# duas ordens, o que torna a matriz simétrica.
