# Exercício 3 — Distância Euclidiana com três atributos
# Atributos: nota média, frequência (%) e horas de estudo por semana.
# Restrição: não utilizar funções prontas de distância.

aluno_a = [8.0, 92, 10]
aluno_b = [7.8, 90, 9]
aluno_c = [5.2, 68, 3]


def distancia_euclidiana_manual(p, q):
    """Distância Euclidiana calculada manualmente (sem funções prontas)."""
    soma_quadrados = 0
    for i in range(len(p)):
        diferenca = p[i] - q[i]
        quadrado = diferenca ** 2
        soma_quadrados += quadrado
    return soma_quadrados ** 0.5


# 14. Distância entre A e B
distancia_ab = distancia_euclidiana_manual(aluno_a, aluno_b)

# 15. Distância entre A e C
distancia_ac = distancia_euclidiana_manual(aluno_a, aluno_c)

# 16. Exibindo os dois resultados
print("Aluno A:", aluno_a)
print("Aluno B:", aluno_b)
print("Aluno C:", aluno_c)
print(f"\nDistância A -> B: {distancia_ab:.2f}")
print(f"Distância A -> C: {distancia_ac:.2f}")

# 17. Informando qual aluno está mais próximo de A
if distancia_ab < distancia_ac:
    mais_proximo = "B"
    menor_distancia = distancia_ab
else:
    mais_proximo = "C"
    menor_distancia = distancia_ac

print(f"\nAluno mais próximo de A: {mais_proximo} (distância {menor_distancia:.2f})")

# Observação: a mesma lógica usada em duas dimensões vale para três (ou mais)
# atributos — basta somar o quadrado da diferença de cada atributo e extrair
# a raiz quadrada da soma total.
