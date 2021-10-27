# LINEAR SEARCH

def linear_search(arr,key):
    for ind,elem in enumerate(arr):
        if elem==key:
            return ind+1
    return -1

arr=[8,3,2,4,5,62,11,2,33,65,3,2,1,33,44,32,111,2223,238]

res=linear_search(arr,112)
if res!=-1:
    print(f"Element found at position {res}")
else:
    print("Element not found!!")

# Time Complexity O(N)
# Space Complexity O(1)
