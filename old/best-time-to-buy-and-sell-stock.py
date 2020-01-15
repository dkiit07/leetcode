# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    if len(prices) == 0 or len(prices) == 1:
        return 0
    profit = prices[1] - prices[0]
    min = prices[0]
    max = prices[1]
    min_index = 0
    max_index = 1
    for i in range(1, len(prices)-1):
        if min >= prices[i]:
            min = prices[i]
            min_index = i
        if max <= prices[i+1]:
            max = prices[i+1]
            max_index = i+1
        if min < max and min_index < max_index:
            if profit < max-min:
                profit = max-min

    if profit > 0:
        return profit
    else:
        return 0


# result = maxProfit([7,1,5,3,6,4])
# result = maxProfit([7,6,4,3,1])
# result = maxProfit([2,1,2,0,1])
# result = maxProfit([1,2])
# result = maxProfit([2,1,2,1,0,1,2])
result = maxProfit([3,3,5,0,0,3,1,4])
print(result)