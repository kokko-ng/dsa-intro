"""
Graph helper classes and utilities.
"""
from typing import Optional, List, Dict


class GraphNode:
    """Graph node for adjacency list representation (used in clone graph, etc.)."""

    def __init__(self, val: int = 0, neighbors: Optional[List['GraphNode']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        neighbor_vals = [n.val for n in self.neighbors]
        return f"GraphNode({self.val}, neighbors={neighbor_vals})"


def create_adjacency_list(edges: Dict[int, List[int]]) -> Dict[int, List[int]]:
    """
    Create an adjacency list from an edges dictionary.

    Args:
        edges: Dictionary mapping node -> list of neighbors

    Returns:
        The same adjacency list (for consistency with other helpers)

    Example:
        >>> adj = create_adjacency_list({0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]})
        >>> adj[0]
        [1, 2]
    """
    return edges


def build_graph_from_edges(n: int, edges: List[List[int]], directed: bool = False) -> Dict[int, List[int]]:
    """
    Build adjacency list from edge list.

    Args:
        n: Number of nodes (0 to n-1)
        edges: List of [from, to] edges
        directed: Whether the graph is directed

    Returns:
        Adjacency list

    Example:
        >>> adj = build_graph_from_edges(4, [[0, 1], [1, 2], [2, 3]])
        >>> adj[0]
        [1]
        >>> adj[1]
        [0, 2]
    """
    graph = {i: [] for i in range(n)}

    for edge in edges:
        u, v = edge[0], edge[1]
        graph[u].append(v)
        if not directed:
            graph[v].append(u)

    return graph


def build_graph_nodes(adj_list: List[List[int]]) -> Optional[GraphNode]:
    """
    Build a graph of GraphNode objects from adjacency list.

    Args:
        adj_list: Adjacency list where adj_list[i] contains neighbors of node i+1
                  (1-indexed as commonly used in LeetCode)

    Returns:
        The first node (node 1), or None if empty

    Example:
        >>> # Graph: 1 -- 2
        >>> #         |    |
        >>> #         4 -- 3
        >>> node = build_graph_nodes([[2, 4], [1, 3], [2, 4], [1, 3]])
        >>> node.val
        1
        >>> [n.val for n in node.neighbors]
        [2, 4]
    """
    if not adj_list:
        return None

    # Create all nodes (1-indexed)
    nodes = {i + 1: GraphNode(i + 1) for i in range(len(adj_list))}

    # Connect neighbors
    for i, neighbors in enumerate(adj_list):
        node_val = i + 1
        nodes[node_val].neighbors = [nodes[n] for n in neighbors]

    return nodes[1]


def graph_to_adj_list(node: Optional[GraphNode]) -> List[List[int]]:
    """
    Convert a graph of GraphNode objects back to adjacency list.

    Args:
        node: Starting node of the graph

    Returns:
        Adjacency list representation
    """
    if not node:
        return []

    # BFS to collect all nodes
    visited = {}
    queue = [node]
    visited[node.val] = node

    while queue:
        current = queue.pop(0)
        for neighbor in current.neighbors:
            if neighbor.val not in visited:
                visited[neighbor.val] = neighbor
                queue.append(neighbor)

    # Build adjacency list (sorted by node value)
    max_val = max(visited.keys())
    adj_list = [[] for _ in range(max_val)]

    for val in range(1, max_val + 1):
        if val in visited:
            adj_list[val - 1] = sorted([n.val for n in visited[val].neighbors])

    return adj_list
