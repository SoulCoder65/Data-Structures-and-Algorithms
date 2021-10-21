# Implementing Binary Search Tree

class BST:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None


# Insertion
def insertOperation(rootNode,data):
    if rootNode.data == None:
        rootNode.data=data
    else:
        if data <= rootNode.data:
            if rootNode.leftChild is None:
                rootNode.leftChild=BST(data)
            else:
                insertOperation(rootNode.leftChild,data)
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild=BST(data)
            else:
                insertOperation(rootNode.rightChild,data)
    return "Node Added Successfully"

newBst=BST(None)
print(insertOperation(newBst,50))
print(insertOperation(newBst,10))
print(insertOperation(newBst,60))