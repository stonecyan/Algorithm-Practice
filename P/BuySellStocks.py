# O(n) runtime
def get_max_profit(arr):
    minPrice = arr[0]
    maxProfit = arr[1] - arr[0]
    for time in range(1, len(arr)):
        profit = arr[time] - minPrice
        if profit > maxProfit:
            maxProfit = profit
        if arr[time] < minPrice:
            minPrice = arr[time]
    return maxProfit


stock_prices = [10, 7, 5, 8, 11, 9]
stock_prices1 = [10, 9, 8, 7, 6, 5]

x = get_max_profit(stock_prices)
x1 = get_max_profit(stock_prices1)
print(x)
print(x1)
