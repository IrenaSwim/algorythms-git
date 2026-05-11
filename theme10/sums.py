def max_sum_cases(n):
    dp =[[0] * (n + 1) for _ in range(n + 1)]
    for m in range(n + 1):
        dp[0][m] = 1
    for i in range(1, n + 1):
        for m in range(1, n + 1):
            dp[i][m] = dp[i][m - 1]
            if m <= i:
                dp[i][m] += dp[i - m][m]
    return dp[n][n]
    
print(max_sum_cases(8))