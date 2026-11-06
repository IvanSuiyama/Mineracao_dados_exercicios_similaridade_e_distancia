# Exercício 4 — Comparando vários clientes com math.dist()
# Atributos: idade e compras por mês.

# 18. Importando o módulo math
import math

clientes = {
    "A": [25, 2],
    "B": [27, 3],
    "C": [30, 5],
    "D": [45, 10],
    "E": [52, 12],
}

# 19. Calculando com math.dist() a distância de A para B, C, D e E
referencia = clientes["A"]
distancias = {}

for nome, valores in clientes.items():
    if nome == "A":
        continue  # não comparar A com ele mesmo
    distancias[nome] = math.dist(referencia, valores)

# 20. Exibindo cada distância calculada
print("Distâncias de A para os demais clientes:")
for nome, distancia in distancias.items():
    print(f"  A -> {nome}: {distancia:.2f}")

# 21. Identificando automaticamente o cliente mais próximo de A
cliente_mais_proximo = min(distancias, key=distancias.get)

print(
    f"\nO cliente com o perfil mais próximo de A é {cliente_mais_proximo} "
    f"(distância {distancias[cliente_mais_proximo]:.2f}), "
    "considerando idade e compras por mês."
)
