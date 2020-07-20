class Graph:

    graph_dict = {}

    def addEdge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        else:
            self.graph_dict[node].append(neighbour)

    def showEdges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(", node, ",", neighbour, ")")

    def findPath(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path

        for node in self.graph_dict[start]:
            if node not in path:
                newPath = self.findPath(node, end, path)
                if newPath:
                    return newPath
                return None


g = Graph()
g.addEdge('1', '2')
g.addEdge('1', '3')
g.addEdge('2', '3')
g.addEdge('2', '1')
g.addEdge('3', '1')
g.addEdge('3', '2')
g.addEdge('3', '4')
g.addEdge('4', '3')

print(g.findPath('2', '4'))
