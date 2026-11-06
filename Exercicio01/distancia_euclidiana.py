# Exercício 1 — Distância Euclidiana entre dois clientes
# Atributos: idade e número de compras por mês.
# Restrição: não utilizar math.dist() nem funções prontas de distância.

# 1. Armazenando os dados dos clientes em listas
cliente_a = [25, 2]
cliente_b = [28, 6]

# 2. Diferença entre as idades
diff_idade = cliente_a[0] - cliente_b[0]

# 3. Diferença entre as quantidades de compras
diff_compras = cliente_a[1] - cliente_b[1]

# 4. Elevando cada diferença ao quadrado
quadrado_idade = diff_idade ** 2
quadrado_compras = diff_compras ** 2

# 5. Somando os resultados
soma = quadrado_idade + quadrado_compras

# 6. Calculando a raiz quadrada da soma
distancia = soma ** 0.5

# 7. Exibindo a distância Euclidiana
print("Cliente A:", cliente_a)
print("Cliente B:", cliente_b)
print(f"Diferença de idade: {diff_idade}")
print(f"Diferença de compras: {diff_compras}")
print(f"Soma dos quadrados: {soma}")
print(f"Distância Euclidiana entre A e B: {distancia:.2f}")
