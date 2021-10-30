from collections import defaultdict

class Graph:
    def __init__(self,num_vertex):
        self.graph=defaultdict(list)
        self.numVertex=num_vertex

    def addVertex(self,vertex,edge):
        self.graph[vertex].append(edge)

    def topologicalSortHelper(self,i,visited,stack):
        visited.append(i)
        for item in self.graph[i]:
            if item not in visited:
                self.topologicalSortHelper(item,visited,stack)

        stack.insert(0,i)

    def topologysort(self):
        visted=[]
        stack=[]
        for k in list(self.graph):
            if k not in visted:
                self.topologicalSortHelper(k,visted,stack)

        print(stack)



graph=Graph(8)
graph.addVertex("A","C")
graph.addVertex("B","C")
graph.addVertex("B","D")
graph.addVertex("C","E")
graph.addVertex("E","H")
graph.addVertex("E","F")
graph.addVertex("D","F")
graph.addVertex("F","G")

print(graph.graph)
graph.topologysort()
