# Exercícios de Similaridade e Distância em Python

Resolução da lista de exercícios de fixação sobre **similaridade e distância**, com implementações manuais da distância Euclidiana e, depois, o uso de funções prontas (`math.dist`) e bibliotecas de ciência de dados (`pandas` e `scikit-learn`).

O objetivo é consolidar a ideia de que, em Mineração de Dados, **quanto menor a distância entre dois registros, mais semelhantes eles são** segundo os atributos considerados.

---

## Sumário

- [Conteúdo abordado](#conteúdo-abordado)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Requisitos](#requisitos)
- [Como executar](#como-executar)
- [Exercícios](#exercícios)
  - [Exercício 1 — Distância Euclidiana entre dois clientes](#exercício-1--distância-euclidiana-entre-dois-clientes)
  - [Exercício 2 — Qual cliente é mais semelhante ao cliente A?](#exercício-2--qual-cliente-é-mais-semelhante-ao-cliente-a)
  - [Exercício 3 — Distância Euclidiana com três atributos](#exercício-3--distância-euclidiana-com-três-atributos)
  - [Exercício 4 — Comparando vários clientes com math.dist()](#exercício-4--comparando-vários-clientes-com-mathdist)
  - [Exercício 5 — Influência da escala e normalização](#exercício-5--influência-da-escala-e-normalização)
  - [Exercício 6 — Matriz de distâncias entre registros](#exercício-6--matriz-de-distâncias-entre-registros)
- [Resultados consolidados](#resultados-consolidados)
- [Conceitos importantes](#conceitos-importantes)
- [Observações](#observações)

---

## Conteúdo abordado

- Cálculo manual da distância Euclidiana em 2 e 3 dimensões;
- Comparação de registros e identificação do vizinho mais próximo;
- Uso de `math.dist()` para automatizar o cálculo;
- Diferença entre atributos em escalas distintas;
- Normalização de dados com `MinMaxScaler`;
- Construção de matriz de distâncias com `pandas`;
- Propriedades da matriz de distâncias: diagonal nula e simetria.

---

## Estrutura do repositório

```
.
├── Exercicio01/
│   └── distancia_euclidiana.py
├── Exercicio02/
│   └── cliente_mais_semelhante.py
├── Exercicio03/
│   └── tres_atributos.py
├── Exercicio04/
│   └── math_dist.py
├── Exercicio05/
│   └── escala_normalizacao.py
├── Exercicio06/
│   └── matriz_distancias.py
├── .gitignore
└── README.md
```

Cada exercício fica em sua própria pasta e pode ser executado de forma independente.

---

## Requisitos

- **Python 3.10+** (testado com Python 3.13)
- Para os exercícios 1 a 4: apenas a biblioteca padrão (`math`);
- Para os exercícios 5 e 6:

```bash
pip install pandas scikit-learn
```

---

## Como executar

Na raiz do projeto:

```bash
python3 Exercicio01/distancia_euclidiana.py
python3 Exercicio02/cliente_mais_semelhante.py
python3 Exercicio03/tres_atributos.py
python3 Exercicio04/math_dist.py
python3 Exercicio05/escala_normalizacao.py
python3 Exercicio06/matriz_distancias.py
```

Ou, para executar todos de uma vez:

```bash
for d in Exercicio0{1..6}; do
  echo "=== $d ==="
  python3 "$d"/*.py
done
```

---

## Exercícios

### Exercício 1 — Distância Euclidiana entre dois clientes

**Arquivo:** `Exercicio01/distancia_euclidiana.py`

Compara dois clientes usando **idade** e **número de compras por mês**:

```python
cliente_a = [25, 2]
cliente_b = [28, 6]
```

O cálculo é feito passo a passo, sem funções prontas:

1. diferença entre as idades: `25 - 28 = -3`;
2. diferença entre as compras: `2 - 6 = -4`;
3. quadrado de cada diferença: `9` e `16`;
4. soma dos quadrados: `25`;
5. raiz quadrada da soma: `5`.

**Resultado:** distância Euclidiana entre A e B = **5.00**.

---

### Exercício 2 — Qual cliente é mais semelhante ao cliente A?

**Arquivo:** `Exercicio02/cliente_mais_semelhante.py`

O cliente A (`[25, 2]`) é usado como referência para comparar com B, C e D. A distância é calculada manualmente por uma função própria, que percorre os atributos, soma os quadrados das diferenças e extrai a raiz.

| Comparação | Distância |
|---|---:|
| A → B | 2.24 |
| A → C | 21.54 |
| A → D | 28.79 |

**Resultado:** o cliente **B** é o mais próximo de A, com distância **2.24**.

O código contém um comentário explicando que a menor distância indica maior semelhança porque significa menor diferença nos atributos analisados (idade e compras por mês).

---

### Exercício 3 — Distância Euclidiana com três atributos

**Arquivo:** `Exercicio03/tres_atributos.py`

Compara três alunos usando **nota média**, **frequência (%)** e **horas de estudo por semana**:

```python
aluno_a = [8.0, 92, 10]
aluno_b = [7.8, 90, 9]
aluno_c = [5.2, 68, 3]
```

| Comparação | Distância |
|---|---:|
| A → B | 2.24 |
| A → C | 25.16 |

**Resultado:** o aluno **B** está mais próximo de A.

O exercício demonstra que a mesma lógica de duas dimensões se generaliza para três ou mais atributos: soma-se o quadrado da diferença de cada atributo e calcula-se a raiz quadrada do total.

---

### Exercício 4 — Comparando vários clientes com `math.dist()`

**Arquivo:** `Exercicio04/math_dist.py`

Utiliza a função pronta `math.dist()` para calcular automaticamente as distâncias de A para os demais clientes:

```python
clientes = {
    "A": [25, 2],
    "B": [27, 3],
    "C": [30, 5],
    "D": [45, 10],
    "E": [52, 12],
}
```

| Comparação | Distância |
|---|---:|
| A → B | 2.24 |
| A → C | 5.83 |
| A → D | 21.54 |
| A → E | 28.79 |

**Resultado:** o cliente **B** possui o perfil mais próximo de A, considerando idade e compras por mês. O cliente mais próximo é identificado automaticamente com `min()` sobre o dicionário de distâncias.

---

### Exercício 5 — Influência da escala e normalização

**Arquivo:** `Exercicio05/escala_normalizacao.py`

Cria um `DataFrame` com **Idade** e **Renda (R$)** e calcula a distância entre A e B antes e depois da normalização.

| Cliente | Idade | Renda (R$) |
|---|---:|---:|
| A | 20 | 2.000 |
| B | 25 | 3.000 |
| C | 40 | 6.000 |
| D | 55 | 9.000 |
| E | 70 | 12.000 |

**Valores originais:**

```
Distância A-B = 1000.01
```

**Valores normalizados com `MinMaxScaler`:**

| Cliente | Idade | Renda |
|---|---:|---:|
| A | 0.0 | 0.0 |
| B | 0.1 | 0.1 |
| C | 0.4 | 0.4 |
| D | 0.7 | 0.7 |
| E | 1.0 | 1.0 |

```
Distância A-B = 0.1414
```

**Por que a renda domina na distância original?**

A distância Euclidiana usa os valores absolutos de cada atributo. A renda varia na casa dos milhares (`2000` a `12000`), enquanto a idade varia na casa das dezenas (`20` a `70`). A diferença de renda entre A e B é `1000`, enquanto a diferença de idade é apenas `5`. Assim, o termo da renda ao quadrado domina completamente o resultado. Após a normalização MinMax, ambas as colunas passam a variar entre `0` e `1`, e os atributos contribuem de forma equilibrada para a distância.

---

### Exercício 6 — Matriz de distâncias entre registros

**Arquivo:** `Exercicio06/matriz_distancias.py`

Calcula a distância Euclidiana entre todos os pares de registros com `math.dist()` e monta uma matriz com `pandas.DataFrame`:

```python
registros = {
    "A": [1, 1],
    "B": [4, 5],
    "C": [2, 2],
    "D": [5, 4],
}
```

**Matriz de distâncias:**

|   | A | B | C | D |
|---|---:|---:|---:|---:|
| **A** | 0.00 | 5.00 | 1.41 | 5.00 |
| **B** | 5.00 | 0.00 | 3.61 | 1.41 |
| **C** | 1.41 | 3.61 | 0.00 | 3.61 |
| **D** | 5.00 | 1.41 | 3.61 | 0.00 |

- **Menor distância diferente de zero:** 1.41;
- **Par mais próximo:** **A e C**;
- **Diagonal principal apenas com zeros:** `True`;
- **Matriz simétrica:** `True`.

**Por que a diagonal é zero?**
Cada registro comparado consigo mesmo não possui diferença em nenhum atributo; logo, a soma dos quadrados é zero e a raiz também.

**Por que `d(A, B) = d(B, A)`?**
Cada termo usa `(a_i - b_i)²`, e `(a_i - b_i)² = (b_i - a_i)²`. Como a soma e a raiz são as mesmas nas duas ordens, a matriz resultante é simétrica.

---

## Resultados consolidados

| Exercício | Tema | Resultado principal |
|---|---|---|
| 01 | Distância manual em 2D | A–B = **5.00** |
| 02 | Cliente mais semelhante | **B** (2.24) |
| 03 | Distância manual em 3D | **B** (2.24) vs. C (25.16) |
| 04 | `math.dist()` | **B** (2.24) |
| 05 | Escala e normalização | 1000.01 → **0.1414** |
| 06 | Matriz de distâncias | **A–C** (1.41); matriz simétrica |

---

## Conceitos importantes

### Distância Euclidiana

Para dois pontos \(p\) e \(q\) com \(n\) atributos:

\[
d(p, q) = \sqrt{\sum_{i=1}^{n} (p_i - q_i)^2}
\]

Em Python, o cálculo manual pode ser escrito como:

```python
soma = 0
for i in range(len(p)):
    soma += (p[i] - q[i]) ** 2
distancia = soma ** 0.5
```

### Similaridade e distância

A distância Euclidiana é uma medida de **dissimilaridade**: valores menores indicam registros mais parecidos. Por isso, o vizinho mais próximo é aquele com a menor distância em relação à referência.

### Normalização MinMax

O `MinMaxScaler` transforma cada atributo para o intervalo \([0, 1]\):

\[
x' = \frac{x - x_{min}}{x_{max} - x_{min}}
\]

Isso evita que atributos com escalas maiores (como renda em reais) dominem o cálculo da distância.

### Matriz de distâncias

Uma matriz de distâncias \(D\) tem \(D_{ij} = d(i, j)\). Suas propriedades básicas são:

- **Diagonal nula:** \(D_{ii} = 0\);
- **Simetria:** \(D_{ij} = D_{ji}\);
- **Não negatividade:** \(D_{ij} \ge 0\).

---

## Observações

- Nos exercícios 1, 2 e 3 foi respeitada a restrição de **não utilizar funções prontas de distância**; o cálculo é feito manualmente com operações básicas.
- Nos exercícios 4, 5 e 6 foi utilizada `math.dist()`, conforme solicitado.
- Os exercícios 5 e 6 dependem de `pandas` e `scikit-learn`.
- Os arquivos `Lista_Exercicios_Similaridade_Distancia.pdf` e `repo.txt` são locais e estão listados no `.gitignore`, não sendo versionados.

---

## Autor

**Ivan Suiyama** — exercícios desenvolvidos para a disciplina de Mineração de Dados.
