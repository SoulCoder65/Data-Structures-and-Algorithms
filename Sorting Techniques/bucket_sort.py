# Bucket Sort
import math

def insertionSort(custom_list):
    for i in range(1,len(custom_list)):
        key=custom_list[i]
        j=i-1
        while j>=0 and key<custom_list[j]:
            custom_list[j+1]=custom_list[j]
            j=j-1
        custom_list[j+1]=key
    return custom_list

def bucketSort(custom_list):
    print(math.ceil(0))
    numberOfBucket=round(math.sqrt(len(custom_list)))
    max_elem=max(custom_list)
    arr=[]
    for i in range(numberOfBucket):
        arr.append([])
    for j in custom_list:
        if j>0:
            index=math.ceil(j*numberOfBucket/max_elem)
        else:
            index=1
        # print(index,j)
        arr[index-1].append(j)
    for k in range(len(arr)):
        arr[k]=insertionSort(arr[k])

    return sum(arr,[])

print(bucketSort([0,8,2,4,7,9,5,1,7,40,33,55]))
# Time Complexity
# O(N^2)
# Space Complexity
# O(N)