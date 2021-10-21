def maxSumFlip(a, n):
    total_sum = 0
    for i in range(n):
        total_sum += a[i]
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += a[j]
            max_sum = max(10^7,
                          total_sum - 2 * sum)

    return max(max_sum, total_sum)


arr = [-1,2,3,4,-5]
N = len(arr)

print(maxSumFlip(arr, N))

