from collections import defaultdict

def to_adjlist(matrix):
    graph = defaultdict(list)
    edges = set()

    for src, index in enumerate(matrix, 1):
        for dst, cost in enumerate(index, 1):
            if cost != 0 and frozenset([src, dst]) not in edges:
                edges.add(frozenset([src, dst]))

                # append to both ends
                graph[src].append((dst, cost))
                graph[dst].append((src, cost))
        
    return graph