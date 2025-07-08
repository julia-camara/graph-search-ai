import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from utils.prompt_parser import extract_edges, extract_operation_type, extract_bfs_params, extract_parent_node
from collections import deque

def build_graph(edges):
    graph = {}
    for src, dst in edges:
        graph.setdefault(src, []).append(dst)
    return graph


def bfs(graph, start_node, depth):
    visited = set([start_node])
    queue = deque([(start_node, 0)])
    result = set()

    while queue:
        node, d = queue.popleft()

        if d == depth:
            result.add(node)
        elif d < depth:
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, d + 1))

    result.discard(start_node)
    return list(result)

def find_parents(graph, target_node):
    return [src for src, dsts in graph.items() if target_node in dsts]

def process_prompts():
    df = pd.read_csv("prompts.csv")
    results = []

    for _, row in df.iterrows():
        prompt_id = row["prompt_id"]
        problem_type = row["problem_type"]
        prompt = row["prompt"]
        expected = row["answer_nodes"].strip("[]").replace("'", "").split()

        edges = extract_edges(prompt)
        graph = build_graph(edges)
        operation = extract_operation_type(prompt)

        if operation == "bfs":
            start_node, depth = extract_bfs_params(prompt)
            predicted = bfs(graph, start_node, depth)
        elif operation == "parents":
            target_node = extract_parent_node(prompt)
            predicted = find_parents(graph, target_node)
        else:
            predicted = []

        is_correct = set(expected) == set(predicted)
        results.append({
            "prompt_id": prompt_id,
            "problem_type": problem_type,
            "expected": expected,
            "predicted": predicted,
            "is_correct": is_correct
        })
        
    pd.DataFrame(results).to_csv("classic_ai/classic_ai_answers.csv", index=False)

if __name__ == "__main__":
    process_prompts()
