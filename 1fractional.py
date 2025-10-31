def knapSack(W, wt, val, n):
    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]




n = int(input("Enter number of items: "))

val = []
wt = []

print("\nEnter profit and weight for each item:")
for i in range(n):
    profit = int(input(f"Profit of item {i+1}: "))
    weight = int(input(f"Weight of item {i+1}: "))
    val.append(profit)
    wt.append(weight)

W = int(input("\nEnter bag capacity: "))


print("\nMaximum Profit:", knapSack(W, wt, val, n))
