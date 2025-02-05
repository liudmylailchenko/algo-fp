import heapq
import uuid
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import deque


class HeapNode:
    def __init__(self, key, color="#1296F0"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())
        self.left = None
        self.right = None


def build_heap_tree(heap: list):
    if not heap:
        return None

    nodes = [HeapNode(val) for val in heap]

    for i in range(len(nodes)):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2

        if left_idx < len(nodes):
            nodes[i].left = nodes[left_idx]
        if right_idx < len(nodes):
            nodes[i].right = nodes[right_idx]

    return nodes[0]


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=str(node.val))
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph


def generate_colors(n):
    colors = [
        "#{:02X}{:02X}{:02X}".format(
            int(255 - i * (200 / n)), int(50 + i * (100 / n)), 240
        )
        for i in range(n)
    ]
    return colors


def bfs_traverse(tree_root):
    if not tree_root:
        return

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    order = []
    queue = deque([tree_root])
    visited = set()
    while queue:
        node = queue.popleft()
        if node.id in visited:
            continue
        visited.add(node.id)
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    colors = generate_colors(len(order))
    for i, node in enumerate(order):
        node.color = colors[i]
        draw_heap_with_colors(tree_root)


def dfs_traverse(tree_root):
    if not tree_root:
        return

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    order = []
    stack = [tree_root]
    visited = set()
    while stack:
        node = stack.pop()
        if node.id in visited:
            continue
        visited.add(node.id)
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    colors = generate_colors(len(order))
    for i, node in enumerate(order):
        node.color = colors[i]
        draw_heap_with_colors(tree_root)


def draw_heap_with_colors(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: str(node[1]["label"])
        for node in tree.nodes(data=True)
        if "label" in node[1]
    }

    plt.figure(figsize=(15, 8))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()
