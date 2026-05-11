def rucksack(W, wt, val, n):
    dp = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 and w == 0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W] 
    
val = [120, 50, 280]
wt = [100, 250, 300]
W = 450
n = len(wt)

print(rucksack(W, wt, val, n))