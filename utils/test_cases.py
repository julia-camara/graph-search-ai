import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classic_ai.classic_ai import bfs, find_parents

def test_bfs():
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": [],
        "D": []
    }
    assert set(bfs(graph, "A", 1)) == {"B", "C"}
    assert set(bfs(graph, "A", 2)) == {"D"}

def test_parents():
    graph = {
        "A": ["B"],
        "C": ["B"],
        "D": ["E"]
    }
    assert set(find_parents(graph, "B")) == {"A", "C"}
    assert find_parents(graph, "E") == ["D"]

def run_tests():
    test_bfs()
    test_parents()
    print("Todos os testes passaram!")

if __name__ == "__main__":
    run_tests()