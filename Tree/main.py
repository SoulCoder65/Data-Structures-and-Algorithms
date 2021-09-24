#Tree
class Treenode:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children

    def __str__(self,level=0):
        ret=" "*level+str(self.data)+"\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret

    def addChild(self,Treenode):
        self.children.append(Treenode)


rootnode=Treenode("Drinks",[])
hot_drinks=Treenode("Hot Drinks",[])
cold_drinks=Treenode("Cold Drinks",[])
rootnode.addChild(hot_drinks)
rootnode.addChild(cold_drinks)

coffee=Treenode("Coffee",[])
tea=Treenode("Tea",[])

hot_drinks.addChild(coffee)
hot_drinks.addChild(tea)

alcholic=Treenode("Alcholic",[])
non_alcholic=Treenode("Non-Alcholic",[])
cold_drinks.addChild(alcholic)
cold_drinks.addChild(non_alcholic)

print(cold_drinks.children[0].data)
