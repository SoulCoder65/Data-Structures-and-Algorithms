# Binary  Tree using linked list
class BinaryTNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

def preorderTraversal(node):
    if not node:
        return
    else:
        print(node.data)
        preorderTraversal(node.leftChild)
        preorderTraversal(node.rightChild)

def inOrderTraversal(node):
    if not node:
        return
    else:
        inOrderTraversal(node.leftChild)
        print(node.data)
        inOrderTraversal(node.rightChild)

def postOrderTraversal(node):
    if not node:
        return
    else:
        postOrderTraversal(node.leftChild)
        postOrderTraversal(node.rightChild)
        print(node.data)
def levelOrderTraversal(node):
    if not node:
        return
    else:
        queue=[]
        queue.append(node)
        while not len(queue)==0:
            rootnode=queue.pop(0)
            print(rootnode.data)
            if rootnode.leftChild is not None:
                queue.append(rootnode.leftChild)
            if rootnode.rightChild is not None:
                queue.append(rootnode.rightChild)

rootNode=BinaryTNode("Drinks")
leftNode=BinaryTNode("Hot Drinks")

hot1=BinaryTNode("Coffee")
hot2=BinaryTNode("Tea")
leftNode.leftChild=hot1
leftNode.rightChild=hot2


rightNode=BinaryTNode("Cold Drinks")
cold1=BinaryTNode("Ice Tea")
cold2=BinaryTNode("Juice")
rightNode.leftChild=cold1
rightNode.rightChild=cold2
rootNode.leftChild=leftNode
rootNode.rightChild=rightNode
preorderTraversal(rootNode)
print("\n\n")
inOrderTraversal(rootNode)
print("\n\n")

postOrderTraversal(rootNode)
print("\n")
levelOrderTraversal(rootNode)