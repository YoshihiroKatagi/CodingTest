S = int(input())
mod = 10**9+7

dp = [0]*(10**5)

dp[0] = 0
dp[1] = 0
dp[2] = 0
dp[3] = 1
dp[4] = 1
dp[5] = 1

for i in range(6, S+1):
  dp[i] = sum(dp[:i-2])+1
  dp[i] %= mod

print(dp[S])