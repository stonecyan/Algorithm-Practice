def stockBuySellOnce(prices):
    minimum = float('inf')
    maxProfit = 0
    for i in prices:
        if i < minimum:
            minimum = i
        if (i - minimum) > maxProfit:
            maxProfit = i - minimum
    return maxProfit


x = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
y = stockBuySellOnce(x)
print(y)

