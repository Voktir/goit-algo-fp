import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()

# Функція для побудови дерева з купи
def build_tree_from_heap(heap):
    root = Node(heap[0])
    nodes = [root]
    for i in range(1, len(heap)):
        parent = nodes[(i-1)//2]
        node = Node(heap[i])
        if i % 2 == 0:
            parent.right = node
        else:
            parent.left = node
        nodes.append(node)
    return root

def generate_color(start_color, end_color, step, steps):
    """
    Генерує градієнт кольорів від start_color до end_color.
    """
    start_color = int(start_color.lstrip('#'), 16)
    end_color = int(end_color.lstrip('#'), 16)
    start_r = (start_color >> 16) & 255
    start_g = (start_color >> 8) & 255
    start_b = start_color & 255
    end_r = (end_color >> 16) & 255
    end_g = (end_color >> 8) & 255
    end_b = end_color & 255
    print(step)

    r = round(start_r + (step * (end_r - start_r) / (steps)))
    g = round(start_g + (step * (end_g - start_g) / (steps)))
    b = round(start_b + (step * (end_b - start_b) / (steps)))
    print(r, g, b)
    return f"#{hex(r)[2:].zfill(2)}{hex(g)[2:].zfill(2)}{hex(b)[2:].zfill(2)}"


def dfs(root):
    # Обхід в глибину без рекурсії
    stack = [root]
    visited = set()
    pos = {root.id: (0, 0)}
    tree = nx.DiGraph()
    step = 0
    while stack:
        node = stack.pop()
        if node.id not in visited:
            visited.add(node.id)
            step += 1
            node.color = generate_color("#000080", "#FAD8E6", step, total_nodes)
            tree.add_node(node.id, color=node.color, label=node.val)
            # ... (додавання ребер та оновлення позицій)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return tree, pos

def bfs(root):
    # Обхід в ширину без рекурсії
    queue = deque([root])
    visited = set()
    pos = {root.id: (0, 0)}
    tree = nx.DiGraph()
    step = 0
    while queue:
        node = queue.popleft()
        if node.id not in visited:
            visited.add(node.id)
            step += 1
            node.color = generate_color("#004000", "#AFC0CB", step, total_nodes)
            tree.add_node(node.id, color=node.color, label=node.val)
            # ... (додавання ребер та оновлення позицій)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return tree, pos

# Обчислення загальної кількості вузлів
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Приклад використання
heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
root = build_tree_from_heap(heap)

# Збереження порядкового номера відвіданого вузла
total_nodes = int(count_nodes(root))

# Виклик функції обходу DFS
tree, pos = dfs(root)

# Відображення дерева
draw_tree(root)

# Виклик функції обходу BFS
tree, pos = bfs(root)

# Відображення дерева
draw_tree(root)