graph = [
    [0, 0, 38, 95, 0, 1, 57, 0],
    [0, 0, 0, 0, 79, 0, 36, 19],
    [38, 0, 0, 51, 0, 0, 44, 0],
    [95, 0, 51, 0, 0, 44, 0, 0],
    [0, 79, 0, 0, 0, 93, 41, 48],
    [1, 0, 0, 44, 93, 0, 1, 0],
    [57, 36, 44, 0, 41, 1, 0, 0],
    [0, 19, 0, 0, 48, 0, 0, 0]
]

num_vertices = len(graph)
print(f'Кількість вершин: {num_vertices}')

print('Матриця ваг:')
for row in graph:
    print(row)

# Функція пошуку кореневих вузлів дерев
def find(node, parent):
    # Якщо поточний вузол не є кореневим, то шукаємо його батька
    if parent[node] != node:
        parent[node] = find(parent[node], parent)
    return parent[node]

# Алгоритм Борувки
def boruvka_mst(graph):
    num_vertices = len(graph)
    parent = [i for i in range(num_vertices)]
    mst = []
    num_trees = num_vertices

    while num_trees > 1:
        min_edges = [None] * num_vertices

        # Шукаємо мінімальні ребра для кожного компонента
        for i in range(num_vertices):
            for j in range(num_vertices):
                if graph[i][j] > 0:
                    root_i = find(i, parent)
                    root_j = find(j, parent)
                    if root_i != root_j:
                        if min_edges[root_i] is None or graph[i][j] < min_edges[root_i][2]:
                            min_edges[root_i] = (i, j, graph[i][j])
                        if min_edges[root_j] is None or graph[i][j] < min_edges[root_j][2]:
                            min_edges[root_j] = (i, j, graph[i][j])

        # Додаємо знайдені мінімальні ребра до MST
        for edge in min_edges:
            if edge is not None:
                i, j, weight = edge
                root_i = find(i, parent)
                root_j = find(j, parent)
                if root_i != root_j:
                    mst.append((i, j, weight))
                    parent[root_i] = root_j
                    num_trees -= 1

    # Виводимо MST
    print('Пошук Мінімального остового дерева за алгоритмом Борувки у форматі')
    total_weight = 0
    for edge in mst:
        i, j, weight = edge
        print(f'{i} - {j} : {weight}')
        total_weight += weight

    print(f'Сумарна вага: {total_weight}')

boruvka_mst(graph)