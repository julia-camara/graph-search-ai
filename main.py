from collections import defaultdict, deque
from edges import parents_edges, parents_from_node, parents_depth, parents_answer_nodes, bfs_edges, bfs_from_node, bfs_depth, bfs_answer_nodes

class DirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.reverse_graph = defaultdict(list)

    def add_edge(self, from_node, to_node):
        self.graph[from_node].append(to_node)
        self.reverse_graph[to_node].append(from_node)

    def find_parents(self, node):
        return list(set(self.reverse_graph.get(node, [])))

    def bfs_depth_limited(self, start_node, depth):
        visited = set()
        queue = deque([(start_node, 0)])
        result = set()

        while queue:
            current_node, current_depth = queue.popleft()
            if current_depth == depth:
                result.add(current_node)
                continue
            if current_depth > depth:
                continue
            for neighbor in self.graph.get(current_node, []):
                if neighbor not in visited or current_depth + 1 <= depth:
                    visited.add(neighbor)
                    queue.append((neighbor, current_depth + 1))

        result.discard(start_node)  # remove o nó inicial se estiver presente
        return list(result)


# --------------------------
# Parents
# --------------------------
for i in range(3):
    graph = DirectedGraph()
    for from_node, to_node in parents_edges[i]:
        graph.add_edge(from_node, to_node)

    parents = graph.find_parents(parents_from_node[i])
    print(f"Exemplo {i + 1} (Parents):\nPais de 8f14e45fce: {parents}\nResultado Esperado:{parents_answer_nodes[i]}\n")
    
# --------------------------
# BSF
# --------------------------
for i in range (3):
    graph = DirectedGraph()
    for from_node, to_node in bfs_edges[i]:
        graph.add_edge(from_node, to_node)

    parents = graph.bfs_depth_limited(bfs_from_node[i], depth=bfs_depth[i])
    print(f"Exemplo {i + 4} (BFS):\nBFS (profundidade {bfs_depth[i]}) de {bfs_from_node[i]}: {parents}\nResultado Esperado:{bfs_answer_nodes[i]}\n")