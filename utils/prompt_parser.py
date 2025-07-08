import re

def extract_edges(prompt):
    match = re.search(
        r"<end example>\s*Here is the graph to operate on:\s*The graph has the following edges:(.*?)Operation:",
        prompt,
        re.DOTALL
    )
    if not match:
        return []

    raw = match.group(1)
    lines = raw.strip().splitlines()
    edges = []
    for line in lines:
        line = line.strip()
        if '->' in line:
            parts = line.split('->')
            if len(parts) == 2:
                src = parts[0].strip()
                dst = parts[1].strip()
                if src and dst:
                    edges.append((src, dst))
                    
    return edges

def extract_operation_type(prompt):
    match = re.search(r"<end example>.*?Operation:\s*(.*?)\n", prompt, re.DOTALL)
    if not match:
        return "unknown"
    
    op_line = match.group(1).strip()
    if op_line.startswith("Perform a BFS"):
        return "bfs"
    elif op_line.startswith("Find the parents"):
        return "parents"
    return "unknown"

def extract_bfs_params(prompt):
    match = re.search(r"<end example>.*?BFS from node (\w+) with depth (\d+)", prompt, re.DOTALL)
    return match.group(1), int(match.group(2))

def extract_parent_node(prompt):
    match = re.search(r"<end example>.*?Operation:\s*Find the parents of node (\w+)", prompt, re.DOTALL)
    if match:
        return match.group(1)
    return None