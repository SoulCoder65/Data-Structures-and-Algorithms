# Bubble Sort

def bubbleSort(unsort_list):
    for i in range(len(unsort_list)-1):
        has_swapped=False
        for j in range(len(unsort_list)-i-1):
            if unsort_list[j]>unsort_list[j+1]:
                has_swapped=True
                unsort_list[j],unsort_list[j+1]=unsort_list[j+1],unsort_list[j]
        if has_swapped==False:
            break
    print(unsort_list)


bubbleSort([8,2,4,7,9,5,0,1,7,40,33,55])

# Time Complexity
# O(N^2)
# Space Complexity
# O(1)