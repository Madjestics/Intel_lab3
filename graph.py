class Graph:
    def __init__(self, numvertex):
        self.adj_matrix = [[-1] * numvertex for x in range(numvertex)]
        self.numvertex = numvertex
        self.vertices = [0]*numvertex


    def set_vertex(self, id, vtx):
        if 0 <= id <= self.numvertex:
            self.vertices[id] = vtx.lower()

    def set_edge(self, frm, to, cost=0):
        frm = self.vertices.index(frm.lower())
        to = self.vertices.index(to.lower())
        self.adj_matrix[frm][to] = cost

    def get_vertex(self):
        return self.vertices

    def get_edges(self):
        edges = []
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if (self.adj_matrix[i][j] != -1):
                    edges.append((self.vertices[i],
                                  self.vertices[j],
                                  self.adj_matrix[i][j]))
        return edges

    def get_matrix(self):
        return self.adj_matrix

    def get_near_vtx(self, vtx):
        vertex = []
        for i in range(self.numvertex):
            if (self.adj_matrix[vtx][i]!=-1):
                vertex.append(i)
        return vertex

    # Обход в ширину
    def BFS(self, s, goal='0'):
        # Пометить все вершины как не посещённые
        visited = [False] * len(self.vertices)
        s = self.vertices.index(s)

        # Создание очереди для BFS
        queue = []

        # Пометить исходный узел как посещённый
        # и поставить его в очередь
        queue.append(s)
        visited[s] = True

        while queue:

            # Удалить вершину из
            # очереди и вывести её
            s = queue.pop(0)
            if self.vertices[s]==goal:
                return True

            print (self.vertices[s], end = " ")

            # Получить все смежные вершины отложенной вершины s.
            # Если смежная вершина не была посещена, то пометить
            # её посещённой и поставить в очередь
            for i in self.get_near_vtx(s):
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

