import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def build_heap_tree(heap):
    nodes = [Node(val) for val in heap]

    for i in range(len(heap)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(heap):
            nodes[i].left = nodes[left_index]
        if right_index < len(heap):
            nodes[i].right = nodes[right_index]

    return nodes[0] if nodes else None

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def get_color(step, total_steps):
    color_intensity = int(255 * (step / total_steps))
    return f"#{color_intensity:02x}{color_intensity:02x}ff"

def depth_first_traversal(root):
    stack = [root]
    step = 0
    total_steps = count_nodes(root)

    while stack:
        node = stack.pop()
        if node:
            node.color = get_color(step, total_steps)
            step += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

def breadth_first_traversal(root):
    queue = deque([root])
    step = 0
    total_steps = count_nodes(root)

    while queue:
        node = queue.popleft()
        if node:
            node.color = get_color(step, total_steps)
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def main():
    heap = [0, 1, 3, 4, 5, 10]
    root = build_heap_tree(heap)

    depth_first_traversal(root)
    print("Depth-first traversal visualization:")
    draw_tree(root)

    # Reset colors
    root.color = "skyblue"
    root.left.color = "skyblue"
    root.left.left.color = "skyblue"
    root.left.right.color = "skyblue"
    root.right.color = "skyblue"
    root.right.left.color = "skyblue"

    breadth_first_traversal(root)
    print("Breadth-first traversal visualization:")
    draw_tree(root)


if __name__ == "__main__":
    main()
