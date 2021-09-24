class TreeList:
    def __init__(self,maxsize):
        self.customList=maxsize*[None]
        self.lastIndex=0
        self.maxsize=maxsize


    def insertNode(self,value):
        if self.lastIndex+1==self.maxsize:
            return "BT is full"
        else:
            self.customList[self.lastIndex+1]=value
            self.lastIndex+=1
            return "Element Added Successfully"
    def searchNode(self,value):
        if self.lastIndex==0:
            return "BT is empty"
        else:
            for i in range(len(self.customList)):
                if self.customList[i]==value:
                    return f"{value} found at position {i}"
            else:
                return "Element not found"
    def deleteNode(self,value):
        if self.lastIndex==0:
            return "BT is empty"
        else:
            for i in range(len(self.customList)):
                if self.customList[i]==value:
                    self.customList[i]=self.customList[self.lastIndex]
                    self.customList[self.lastIndex]=None
                    self.lastIndex-=1
                    return "Element Deleted Successfully"
            return "Element Not Found"
    def deleteTree(self):
        self.customList=None
        return "Tree Deleted Successfully"

#   Traversing
    def preorderTraversal(self,index):
        if index>self.lastIndex:
            return "Tree is empty"
        else:
            print(self.customList[index])
            self.preorderTraversal(2*index)
            self.preorderTraversal(2*index+1)

    def inorderTraversal(self,index):
        if index>self.lastIndex:
            return "Tree is empty"
        else:
            self.inorderTraversal(2*index)
            print(self.customList[index])
            self.inorderTraversal(2*index+1)
    def postorderTraversal(self,index):
        if index>self.lastIndex:
            return "Tree is empty"
        else:
            self.postorderTraversal(2*index)
            self.postorderTraversal(2*index+1)
            print(self.customList[index])

tree=TreeList(10)
tree.insertNode("Drinks")
tree.insertNode("Hot Drinks")
tree.insertNode("Cold Drinks")
tree.insertNode("Coffee")
tree.insertNode("Tea")
tree.insertNode("Juice")
tree.insertNode("Water")
print(tree.customList)
print("\n")
# Searching
# print(tree.searchNode("Tea"))

# Deleting
# print(tree.deleteNode("Tea"))
# print(tree.customList)
# tree.deleteNode("Drinks")
# print(tree.customList)

# Deleteing entire Tree
# print(tree.customList)
# print(tree.deleteTree())
# print(tree.customList)

# Traversing
tree.preorderTraversal(1)
print("\n")
tree.inorderTraversal(1)
print("\n")
tree.postorderTraversal(1)
