def birthdayCakeCandles(candles):
    n = len(candles)
    candles.sort()
    for idx, val in enumerate(candles):
        if val == candles[n-1]:
            return n-idx