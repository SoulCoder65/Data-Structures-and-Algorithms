# Breadth First Traversal

class Graph:
    def __init__(self,dict=None):
        if dict is None:
            self.dict={}
        else:
            self.dict=dict

    def addNode(self,vertex,edge):
        self.dict[vertex].append(edge)

    def bfsTraversl(self,vertex):
        visited=[vertex]
        queue=[vertex]
        while queue:
            popVertex=queue.pop(0)
            print(popVertex)
            for item in self.dict[popVertex]:
                if item not in visited:
                    visited.append(item)
                    queue.append(item)

dict={
    "A":["B","C"],
    "B":["A","D","E"],
    "C":["A","E"],
    "D":["B","E","F"],
    "E":["B","C","D"],
    "F":["D","E"]
}
graph=Graph(dict)

print(graph.dict)

print("BFS Traversal")
graph.bfsTraversl("A")