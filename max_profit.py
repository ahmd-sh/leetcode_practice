def max_profit():
    prices = [1,5,6,2,9]
    min_price = prices[0]
    prof = 0
    for p in prices[1:]:
        prof = max(prof, p - min_price)
        min_price = min(min_price, p)

    return prof

print(max_profit())
