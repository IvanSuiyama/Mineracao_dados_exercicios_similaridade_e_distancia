# Exercício 2 — Qual cliente é mais semelhante ao cliente A?
# Atributos: idade e compras por mês.
# Restrição: não utilizar funções prontas de distância.

# Cliente de referência
cliente_a = [25, 2]

clientes = {
    "B": [27, 3],
    "C": [45, 10],
    "D": [52, 12],
}


def distancia_euclidiana_manual(p, q):
    """Calcula a distância Euclidiana passo a passo, sem funções prontas."""
    soma_quadrados = 0
    for i in range(len(p)):
        diferenca = p[i] - q[i]          # diferença em cada atributo
        quadrado = diferenca ** 2         # diferença ao quadrado
        soma_quadrados += quadrado        # soma dos quadrados
    return soma_quadrados ** 0.5          # raiz quadrada da soma


# 8, 9 e 10. Calculando manualmente as distâncias de A para B, C e D
distancias = {}
for nome, valores in clientes.items():
    distancias[nome] = distancia_euclidiana_manual(cliente_a, valores)

# 11 e 12. Comparando os resultados e determinando o mais próximo
cliente_mais_proximo = min(distancias, key=distancias.get)

# 13. Exibindo todas as distâncias e o cliente mais próximo
print("Distâncias em relação ao cliente A:")
for nome, distancia in distancias.items():
    print(f"  A -> {nome}: {distancia:.2f}")

print(f"\nCliente mais próximo de A: {cliente_mais_proximo}")
print(f"Menor distância: {distancias[cliente_mais_proximo]:.2f}")

# Por que a menor distância indica maior semelhança?
# A distância Euclidiana mede o quanto dois registros se afastam nos atributos
# considerados (idade e compras por mês). Quanto menor o valor, menor a
# diferença entre os atributos dos clientes e, portanto, mais parecidos são os
# seus perfis. Assim, o cliente com a menor distância é o mais semelhante ao
# cliente A segundo esses atributos.
