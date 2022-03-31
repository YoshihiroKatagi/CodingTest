N = int(input())

point = []
for i in range(N):
  x, y = map(int, input().split())
  point.append([x, y])

  pointX_conv = []
  pointY_conv = []

for x,y in point:
  pointX_conv.append(x + y)
  pointY_conv.append(x - y)

Xdist_max = abs(max(pointX_conv) - min(pointX_conv))
Ydist_max = abs(max(pointY_conv) - min(pointY_conv))

print(max(Xdist_max, Ydist_max))