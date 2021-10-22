# MERGE SORT

def merge(arr,l,m,r):
    n1=m-l+1
    n2=r-m

    L=[0]*(n1)
    R=[0]*(n2)

    for i in range(0,n1):
        L[i]=arr[l+i]
    for j in range(0,n2):
        R[j]=arr[m+1+j]

    i=0
    j=0
    k=l
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1

def mergeSort(arr,l,r):
    if l<r:
        m=(l+(r-1))//2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)
    return  arr


unsort_arr=[8,2,4,7,9,5,0,1,7,40,33,55]

print(mergeSort(unsort_arr,0,len(unsort_arr)-1))
# Time Complexity
# O(NLOGN)
# Space Complexity
# O(N)