# Selection Sort

def selectionSort(unsort_list):
    for i in range(len(unsort_list)):
        min_index=i
        for j in range(min_index+1,len(unsort_list)):
            if unsort_list[min_index]>unsort_list[j]:
                min_index=j
        unsort_list[i],unsort_list[min_index]=unsort_list[min_index],unsort_list[i]
    print(unsort_list)

selectionSort([8,2,4,7,9,5,0,1,7,40,33,55])
# Time Complexity
# O(N^2)
# Space Complexity
# O(1)