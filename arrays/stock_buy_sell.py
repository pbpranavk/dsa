def max_profit(prices):
    days = len(prices)
    profit = 0

    for i in range(1, days):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit

print(max_profit([100, 180, 260, 310, 40, 535, 695]))

def stock_and_buy(prices):
    n = len(prices)

    if n == 1:
        return

    i = 0
    while i < n-1 :
        while ((i < n-1) and prices[i + 1] <= prices[i]):
            i += 1

        if i == n-1:
            break

        buy = i
        i += 1

        while ((i < n) and (prices[i] >= prices[i - 1])):
            i += 1

        sell = i - 1

        print("Buy on day: ",buy,"\t",
                "Sell on day: ",sell)

stock_and_buy([100, 180, 260, 310, 40, 535, 695])