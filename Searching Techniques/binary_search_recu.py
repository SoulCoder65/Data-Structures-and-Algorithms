# BINARY SEARCH

def binary_search(arr,l,u,elem):

    if u>=l:
        mid=(l+u)//2

        if arr[mid]==elem:
            return mid+1
        elif arr[mid]>elem:
            return binary_search(arr,l,mid-1,elem)
        else:
            return binary_search(arr,mid+1,u,elem)
    else:
        return -1

arr=[1,2,3,4,5,6,7,8,9,10,11]


res=binary_search(arr,0,len(arr)-1,10)
if res!=-1:
    print(f"Element found at position {res}")
else:
    print("Element not found!!")
# Time Complexity O(LOGN)
# Space Complexity O(1)

