
# Graph Implementation using adjacency list

class Graph:
    def __init__(self,dict=None):
        if dict is None:
            self.dict={}
        else:
            self.dict=dict

    def addNode(self,vertex,edge):

        self.dict[vertex].append(edge)


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
graph.addNode("F","G")
print(graph.dict)