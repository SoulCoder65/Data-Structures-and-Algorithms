# Tree Implementation using linked list

# Creating tree node
class TreeNode:
    def __init__(self,value):
        self.value=value
        self.leftChild=None
        self.rightChild=None


#Root node
root_node=TreeNode("Drinks")
# First Level
hot_drinks=TreeNode("Hot Drinks")
cold_drinks=TreeNode("Cold Drinks")
root_node.leftChild=hot_drinks
root_node.rightChild=cold_drinks

# Second Level
coffee=TreeNode("Coffee")
tea=TreeNode("Tea")
hot_drinks.leftChild=coffee
hot_drinks.rightChild=tea

juice=TreeNode("Juice")
water=TreeNode("Water")
cold_drinks.leftChild=juice
cold_drinks.rightChild=water


# Traverse Preorder
def preordertraversal(rootNode):
    if not rootNode:
        return "Binary Tree is empty"
    else:
        print(rootNode.value)
        preordertraversal(rootNode.leftChild)
        preordertraversal(rootNode.rightChild)

# preordertraversal(root_node)

# Traverse inorder
def inordertraversal(rootNode):
    if not rootNode:
        return "Binary Tree is empty"
    else:
        inordertraversal(rootNode.leftChild)
        print(rootNode.value)
        inordertraversal(rootNode.rightChild)

# inordertraversal(root_node)

# Traverse postorder
def postordertraversal(rootNode):
    if not rootNode:
        return "Binary Tree is empty"
    else:
        postordertraversal(rootNode.leftChild)
        postordertraversal(rootNode.rightChild)
        print(rootNode.value)
# postordertraversal(root_node)

# Level Order Traversal
def levelOrdertraversal(rootNode):
    if not rootNode:
        return "Binary Tree is empty"
    else:
        queue=[]
        queue.append(rootNode)
        while not len(queue) ==0:
            root=queue.pop(0)
            print(root.value)
            if root.leftChild is not None:
                queue.append(root.leftChild)
            if root.rightChild is not None:
                queue.append(root.rightChild)
# levelOrdertraversal(root_node)

# Insert node in bt
def insertNode(rootNode,insertedNode):
    if not rootNode:
        rootNode=insertedNode
        return "Element Added Successfully"
    else:
        queue=[]
        queue.append(rootNode)
        while not len(queue)==0:
            root=queue.pop(0)
            if root.leftChild is None:
                root.leftChild=insertedNode
                return "Element Added Successfully"
            else:
                queue.append(root.leftChild)
            if root.rightChild is None:
                root.rightChild=insertedNode
                return "Element Added Successfully"
            else:
                queue.append(root.rightChild)
# inserted_node=TreeNode("Cap Coffee")
# print(insertNode(root_node,inserted_node))
#
# levelOrdertraversal(root_node)

# Search Element in BT
def searchElement(rootNode,searchValue):
    if not rootNode:
        return "BT is empty"
    else:
        queue=[]
        queue.append(rootNode)
        while not len(queue)==0:
            root=queue.pop(0)
            if root.value==searchValue:
                return f"Element Found {searchValue}"
            if root.leftChild is not None:
                if root.leftChild.value==searchValue:
                    return f"Element Found {searchValue}"
                else:
                    queue.append(root.leftChild)
            if root.rightChild is not None:
                if root.rightChild.value==searchValue:
                    return f"Element Found {searchValue}"
                else:
                    queue.append(root.rightChild)
        return "Element Not Found!!"
# print(searchElement(root_node,"Juic"))

# Delete Element in BT
# Find deepest node in BT
def deepestNode(rootNode):
    if not rootNode:
        return "BT is empty"
    else:
        queue=[]
        queue.append(rootNode)
        while not len(queue)==0:
            root=queue.pop(0)
            if root.leftChild is not None:
                queue.append(root.leftChild)
            if root.rightChild is not None:
                queue.append(root.rightChild)
        deepestnode=root.value
        return deepestnode

# print(deepestNode(root_node))

def deletedeepestNode(rootNode,dnode):
    if not rootNode:
        return "BT is empty"
    else:
        queue=[]
        queue.append(rootNode)
        while not len(queue)==0:
            root=queue.pop(0)
            if root.value==dnode:
                root.value=None
                return "Element Deleted Successfully"
            if root.leftChild is not None:
                queue.append(root.leftChild)
            if root.rightChild is not None:
                queue.append(root.rightChild)
        return "Element not found"

def removenode(rootNode,dnode):
    if not  rootNode:
        return "BT is empty"
    else:
        queue=[]
        queue.append(rootNode)
        while not len(queue)==0:
            root=queue.pop(0)
            if root.value==dnode:
                deep=deepestNode(rootNode)
                root.value=deep
                deletedeepestNode(rootNode,deep)
            if root.leftChild is not None:
                queue.append(root.leftChild)
            if root.rightChild is not None:
                queue.append(root.rightChild)

levelOrdertraversal(root_node)
print("---------------------\n\n")
removenode(root_node,"Cold Drinks")
levelOrdertraversal(root_node)