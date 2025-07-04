import random
from collections import defaultdict, deque

# 1. Monta o grafo a partir de uma lista de arestas direcionadas
def build_graph(edge_list):
    graph = defaultdict(list)
    for edge in edge_list:
        src, dst = edge.split("->")
        graph[src.strip()].append(dst.strip())
    return graph

# 2. Busca BFS real usada para gerar resposta esperada e avaliar fitness
def bfs(graph, start_node, depth):
    visited = set()
    queue = deque([(start_node, 0)])
    result = []

    while queue:
        current, d = queue.popleft()
        if d == depth and current != start_node:
            result.append(current)
        elif d < depth:
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, d + 1))
    return result

# 3. Gera lista de nós alcançáveis a partir do start_node
def reachable_nodes(graph, start_node, max_depth=3):
    visited = set()
    queue = deque([(start_node, 0)])
    reachable = set()

    while queue:
        current, depth = queue.popleft()
        if current != start_node:
            reachable.add(current)
        if depth < max_depth:
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
    return list(reachable)

# 4. Função de fitness: mede acerto com relação à BFS real
def fitness_bfs(individual, expected):
    return len(set(individual) & set(expected))

# 5. Algoritmo genético ajustado
def genetic_graph_search(graph, start_node, target_depth, generations=20, pop_size=10):
    expected = bfs(graph, start_node, target_depth)
    nodes = reachable_nodes(graph, start_node, max_depth=target_depth)
    if not nodes:
        return []

    population = [random.sample(nodes, k=min(2, len(nodes))) for _ in range(pop_size)]

    for _ in range(generations):
        scores = [fitness_bfs(ind, expected) for ind in population]
        sorted_population = [ind for _, ind in sorted(zip(scores, population), reverse=True)]
        parents = sorted_population[:pop_size // 2]

        next_gen = []
        while len(next_gen) < pop_size:
            p1, p2 = random.sample(parents, 2)
            child = list(set(p1 + p2))[:2]
            if random.random() < 0.3 and nodes:
                child[random.randint(0, len(child)-1)] = random.choice(nodes)
            next_gen.append(child)

        population = next_gen

    final_scores = [fitness_bfs(ind, expected) for ind in population]
    best = population[final_scores.index(max(final_scores))]
    return best



edges = [
    "uvwx -> alke",
    "abcd -> uvwx",
    "abcd -> efgh",
    "efgh -> uvwx"
]

graph = build_graph(edges)

# Prompt diz: "Perform a BFS from node abcd with depth 1."
result = genetic_graph_search(graph, start_node="abcd", target_depth=1)

print("1. Resultado do algoritmo genético:", result)
# Esperado: ['uvwx', 'efgh']


# Prompt diz: "Perform a BFS from node alke with depth 1."
result = genetic_graph_search(graph, start_node="alke", target_depth=1)

print("2. Resultado do algoritmo genético:", result)
# Esperado: []


# Prompt diz: "Perform a BFS from node uvwx."
result = genetic_graph_search(graph, start_node="uvwx", target_depth=1)

print("3. Resultado do algoritmo genético:", result)
# Esperado: ['abcd', 'efgh']


# Prompt diz: "Perform a BFS from node abcd."
result = genetic_graph_search(graph, start_node="abcd", target_depth=1)

print("4. Resultado do algoritmo genético:", result)
# Esperado: []


edges = [
    "cfcd208495 -> 1679091c5a",
    "cfcd208495 -> cfcd208495",
    "cfcd208495 -> c81e728d9d",
    "cfcd208495 -> c4ca4238a0",
    "c4ca4238a0 -> c9f0f895fb",
    "c4ca4238a0 -> 45c48cce2e",
    "c4ca4238a0 -> eccbc87e4b",
    "c4ca4238a0 -> c9f0f895fb",
    "c81e728d9d -> 45c48cce2e",
    "c81e728d9d -> eccbc87e4b",
    "c81e728d9d -> eccbc87e4b",
    "c81e728d9d -> c9f0f895fb",
    "eccbc87e4b -> d3d9446802",
    "eccbc87e4b -> d3d9446802",
    "eccbc87e4b -> a87ff679a2",
    "eccbc87e4b -> c4ca4238a0",
    "a87ff679a2 -> 1679091c5a",
    "a87ff679a2 -> eccbc87e4b",
    "a87ff679a2 -> cfcd208495",
    "a87ff679a2 -> e4da3b7fbb",
    "e4da3b7fbb -> c4ca4238a0",
    "e4da3b7fbb -> 1679091c5a",
    "e4da3b7fbb -> 1679091c5a",
    "e4da3b7fbb -> 45c48cce2e",
    "1679091c5a -> 8f14e45fce",
    "1679091c5a -> 8f14e45fce",
    "1679091c5a -> e4da3b7fbb",
    "1679091c5a -> a87ff679a2",
    "8f14e45fce -> 45c48cce2e",
    "8f14e45fce -> e4da3b7fbb",
    "8f14e45fce -> 8f14e45fce",
    "8f14e45fce -> cfcd208495",
    "c9f0f895fb -> eccbc87e4b",
    "c9f0f895fb -> cfcd208495",
    "c9f0f895fb -> eccbc87e4b",
    "c9f0f895fb -> 8f14e45fce",
    "45c48cce2e -> cfcd208495",
    "45c48cce2e -> 1679091c5a",
    "45c48cce2e -> a87ff679a2",
    "45c48cce2e -> a87ff679a2",
    "d3d9446802 -> 8f14e45fce",
    "d3d9446802 -> d3d9446802",
    "d3d9446802 -> 45c48cce2e",
    "d3d9446802 -> e4da3b7fb"
]

graph = build_graph(edges)

# Prompt diz: "Perform a BFS from node 8f14e45fce1."
result = genetic_graph_search(graph, start_node="8f14e45fce", target_depth=1)

print("5. Resultado do algoritmo genético:", result)
# Esperado: [ "1679091c5a", "c9f0f895fb", "8f14e45fce", "d3d9446802" ]

