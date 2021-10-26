# # QUICK SORT
#
# def partitionFunction(arr,low,high):
#     i=low-1
#     pivot=arr[high]
#     for j in range(low,high):
#         if arr[j]<=pivot:
#             i=i+1
#             arr[i],arr[j]=arr[j],arr[i]
#     arr[i+1],arr[high]=arr[high],arr[i+1]
#     return (i+1)
#
# def quickSort(arr,low,high):
#     if len(arr)==1:
#         return arr
#     else:
#         if low<high:
#             pi=partitionFunction(arr,low,high)
#             quickSort(arr,low,pi-1)
#             quickSort(arr,pi+1,high)
#     return arr
# unsort_arr=[8,2,4,7,9,5,0,1,7,40,33,55]
#
# print(quickSort(unsort_arr,0,len(unsort_arr)-1))
#
#


# Second Method

def quickSort(arr):
    size=len(arr)
    if size<=1:
        return arr
    else:
        pivot=arr.pop()
    left_sub_list=[]
    right_sub_list=[]

    for item in arr:
        if item<pivot:
            left_sub_list.append(item)
        else:
            right_sub_list.append(item)

    return quickSort(left_sub_list)+[pivot]+quickSort(right_sub_list)

unsort_arr=[8,2,4,7,9,5,0,1,7,40,33,55]
print(quickSort(unsort_arr))