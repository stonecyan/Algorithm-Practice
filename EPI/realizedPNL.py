
def realizedPNL(trans):
    orders = {}
    PNL = 0
    for i in trans:
        tick = i[3]
        print(tick)
        if tick not in orders:
            orders[tick] = []
            orders[tick].append([i[0], str(i[1]), str(i[2])])
        else:
            if i[0] == orders[tick][0][0]:
                orders[tick].append([i[0], str(i[1]), str(i[2])])
            else:
                shares = int(i[2])
                sharePrice = int(i[1])
                mod = 1
                if tick[0] == "SELL":
                    mod = -1
                positionShares = int(orders[tick][0][2])
                positionPrice = int(orders[tick][0][1])
                PNL = PNLCalculation(shares, sharePrice, positionShares, positionPrice, orders, mod, tick)
    return PNL


def PNLCalculation(shares, sharePrice, positionShares, positionPrice, orders, mod, tick):
    PNL = 0
    if mod == 1:
        ordertype = "SELL"
    else:
        ordertype = "BUY"
    if shares < positionShares:

        remainShares = positionShares - shares
        orders[tick][0][2] = remainShares
        return shares * (sharePrice - positionPrice) * mod

    elif shares == positionShares:
        orders[tick].pop(0)
        return shares * (sharePrice - positionPrice) * mod

    elif shares > positionShares:
        remainShares = shares - positionShares
        PNL += positionShares * (sharePrice - positionPrice) * mod
        orders[tick].pop(0)
        if len(orders[tick]) == 0:
            orders[tick].append([ordertype, sharePrice, remainShares])
            return PNL
        PNL += PNLCalculation(remainShares, sharePrice, int(orders[tick][0][2]), int(orders[tick][0][1]), orders, mod, tick)
        return PNL


x = [["BUY", 100, 10, "GOOG"], ["BUY", 100, 10, "GOOG"], ["SELL", 200, 25, "GOOG"], ["SELL", 200, 25, "GOOG"]]
a = realizedPNL(x)
print(a)
