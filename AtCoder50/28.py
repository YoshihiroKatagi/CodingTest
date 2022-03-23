H, W, K = map(int, input().split())

c = []

for gyou in range(H):
  tmp = input()
  tmp = list(tmp)
  c.append(tmp)

ans = 0

for gyou_red in range(1<<H):
  for retu_red in range(1<<W):
    black = 0
    
    for gyou in range(H):
      for retu in range(W):
        if gyou_red>>gyou & 1==0 and retu_red>>retu & 1==0:
          if c[gyou][retu]=="#":
            black += 1
    
    if black==K:
      ans += 1

print(ans)