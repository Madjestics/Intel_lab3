from graph import Graph



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    G = Graph(6)
    G.set_vertex(0, 'a')
    G.set_vertex(1, 'b')
    G.set_vertex(2, 'c')
    G.set_vertex(3, 'd')
    G.set_vertex(4, 'e')
    G.set_vertex(5, 'f')
    G.set_edge('a', 'e', 10)
    G.set_edge('a', 'c', 20)
    G.set_edge('c', 'b', 30)
    G.set_edge('b', 'e', 40)
    G.set_edge('e', 'd', 50)
    G.set_edge('f', 'e', 60)

    print("Вершины графа:")
    print(G.get_vertex())

    print("Рёбра графа:")
    print(G.get_edges())

    print("Матрица смежности:")
    print(G.get_matrix())

    print("Обход в ширину (начиная с вершины 2)")
    G.BFS(2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/