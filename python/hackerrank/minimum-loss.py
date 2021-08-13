def minimumLoss(price):
    n = len(price)
    idx_price = []
    for idx, val in enumerate(price):
        idx_price.append([idx, val])
    idx_price.sort(key = lambda x: -x[1])
    answer = sys.maxsize
    for i in range(n-1):
        if idx_price[i][0] < idx_price[i+1][0]:
            answer = min(answer, idx_price[i][1] - idx_price[i+1][1])
    
    return answer