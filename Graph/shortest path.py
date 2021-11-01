# Shortest path Algorithm using BFS

class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            self.gdict={}
        else:
            self.gdict=gdict


    def bfsShortest(self,start,end):
        queue=[]
        queue.append([start])
        while queue:
            path=queue.pop(0)
            node=path[-1]
            if node==end:
                return path
            else:
                for item in self.gdict[node]:
                    new_path=list(path)
                    print(new_path)
                    new_path.append(item)
                    queue.append(new_path)


customDict={
    "a":["b","c"],
    "b":["d","g"],
    "c":["d","e"],
    "d":["f"],
    "e":["f"],
    "g":["f"]


}
g=Graph(customDict)
print(g.bfsShortest("a","f"))
