N = int(input())
h = [0] + list(map(int, input().split()))

dp = [10**15] * (N+1)

dp[1] = 0
dp[2] = abs(h[2] - h[1])

for i in range(3,N+1):
  cost2 = dp[i-2] + abs(h[i] - h[i-2])
  cost1 = dp[i-1] + abs(h[i] - h[i-1])
  dp[i] = min(cost1, cost2)

print(dp[N])