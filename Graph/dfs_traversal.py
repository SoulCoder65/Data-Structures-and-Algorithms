# Depth First Search

class Graph:
    def __init__(self,dict=None):
        if dict is None:
            self.dict={}
        else:
            self.dict=dict

    def addNode(self,vertex,edge):
        self.dict[vertex].append(edge)

    def dfsTraversal(self,vertex):
        visited=[vertex]
        stack=[vertex]
        while stack:
            popVertex=stack.pop()
            print(popVertex)
            for item in self.dict[popVertex]:
                if item not in visited:
                    visited.append(item)
                    stack.append(item)
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

print("DFS Traversal")
graph.dfsTraversal("A")