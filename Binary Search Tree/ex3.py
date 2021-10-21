
# comb=list(zip(rewards,time_required))
# comb.sort(reverse=True)
# total_time=0
# book_selected=[]
# for item in comb:
#     total_time=total_time+item[1]
#     if total_time<=time_limit:
#         book_selected.append(item[0])
#     else:
#         total_time=total_time-item[1]
# print(sum(book_selected))
def maxProfit(W, wt, val, n):
    if n == 0 or W == 0:
        return 0

    if (wt[n - 1] > W):
        return maxProfit(W, wt, val, n - 1)

    else:
        return max(val[n - 1] + maxProfit(W - wt[n - 1], wt, val, n - 1),
                   maxProfit(W, wt, val, n - 1))


book_num=2
time_limit=5
rewards=[2,4]
time_required=[3,5]

print(maxProfit(time_limit, time_required, rewards, book_num))
