H, W, X, Y = map(int, input().split())
grid = []
for i in range(H):
  S = input()
  S = list(S)
  grid.append(S)

X-=1
Y-=1

ans = 0

#上
for i in range(1,H):
  if 0<=X-i<H:
    if grid[X-i][Y] == "#":
      break
    else:
      ans+=1

#下
for i in range(1,H):
  if 0<=X+i<H:
    if grid[X+i][Y] == "#":
      break
    else:
      ans+=1

#左
for i in range(1,W):
  if 0<=Y-i<W:
    if grid[X][Y-i] == "#":
      break
    else:
      ans+=1

#右
for i in range(1,W):
  if 0<=Y+i<W:
    if grid[X][Y+i] == "#":
      break
    else:
      ans+=1

ans+=1

print(ans)