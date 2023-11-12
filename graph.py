class Graph:
    def __init__(self, numvertex):
        self.adj_matrix = [[-1] * numvertex for x in range(numvertex)]
        self.vertices = []
        self.numvertex = numvertex

    def set_vertex(self, vtx):
        if vtx.lower() not in self.vertices:
            self.vertices.append(vtx.lower())

    def set_edge(self, frm, to, cost=0):
        frm = self.vertices.index(frm.lower())
        to = self.vertices.index(to.lower())
        self.adj_matrix[frm][to] = cost
        if cost=='is a':
            self.adj_matrix[to][frm] = cost

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

    def get_vertex_for_ako(self, vrtx):
        vertex = []
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if (self.adj_matrix[i][vrtx]=='ako'):
                    vertex.append(self.vertices[i])
                    break
        return vertex

    # Обход в ширину
    def BFS(self, start, goal, connection):
        visited = [False] * len(self.vertices)
        s = self.vertices.index(start)
        queue = []
        edges = []
        res = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)

            #для случая с какие
            if start==goal:
                if s < self.vertices.index(start):
                    continue
                vertex = self.get_vertex_for_ako(s)
                for i in range(len(vertex)):
                    res.append(vertex[i])
            #для остальных вопросов
            elif self.vertices[s]==goal and connection in edges:
                return True
            for i in self.get_near_vtx(s):
                if visited[i] == False:
                    queue.append(i)
                    edges.append(self.adj_matrix[s][i])
                    visited[i] = True
        return res

