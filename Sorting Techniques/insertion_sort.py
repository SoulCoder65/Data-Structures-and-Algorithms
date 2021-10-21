# Insertion Sort

def insertSort(unsort_list):
    for i in range(1,len(unsort_list)):
        key=unsort_list[i]
        j=i-1
        while j>=0 and key<unsort_list[j]:
            unsort_list[j+1]=unsort_list[j]
            j=j-1
        unsort_list[j+1]=key
    print(unsort_list)

insertSort([8,2,4,7,9,5,0,1,7,40,33,55])
# Time Complexity
# O(N^2)
# Space Complexity
# O(1)