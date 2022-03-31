N, W = map(int, input().split())
items = [[0, 0]]
for i in range(N):
  w, v = map(int, input().split())
  items.append([w,v])

dp = [[0]*(W+1) for i in range(N+1)]

for gyou_i in range(1, N+1):
  for retu_w in range(W+1):
    w, v = items[gyou_i]
    if retu_w - w < 0:
      dp[gyou_i][retu_w] = dp[gyou_i - 1][retu_w]
    else:
      red = dp[gyou_i - 1][retu_w]
      blue = dp[gyou_i - 1][retu_w - w] + v
      dp[gyou_i][retu_w] = max(red, blue)

print(dp[N][W])