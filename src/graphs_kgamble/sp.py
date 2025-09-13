import sys
from .heapq import heappush, heappop

def dijkstra(graph, source):
    """
    Dijkstra's shortest path using a min-heap.
    graph: dict[int, dict[int, int]] adjacency with weights
    source: int starting vertex
    Returns: (dist, path) where
      dist is a list of distances such that dist[v] is min cost from source to v
      path is a dict where path[v] is the list of nodes from source to (but not including) v
    """
    n = max(graph.keys()) + 1 if graph else 0
    dist = [sys.maxsize] * n
    dist[source] = 0
    heap = []
    heappush(heap, (0, source))
    path = {source: []}

    while heap:
        w, u = heappop(heap)
        if w > dist[u]:
            continue
        for v in graph.get(u, {}):
            cand = w + graph[u][v]
            if cand < dist[v]:
                dist[v] = cand
                heappush(heap, (cand, v))
                path[v] = path[u] + [u]
    return dist, path
