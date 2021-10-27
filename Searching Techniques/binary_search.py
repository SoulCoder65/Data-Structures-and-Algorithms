# BINARY SEARCH

def binary_search(arr,key):
    l=0
    u=len(arr)-1
    while l<=u:
        mid=(l+u)//2
        if arr[mid]==key:
            return mid+1
        else:
            if key<arr[mid]:
                u=mid-1
            else:
                l=mid+1
    return -1

arr=[1,2,3,4,5,6,7,8,9,10,11]


res=binary_search(arr,10)
if res!=-1:
    print(f"Element found at position {res}")
else:
    print("Element not found!!")
# Time Complexity O(LOGN)
# Space Complexity O(1)
