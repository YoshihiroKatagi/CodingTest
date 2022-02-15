import math

a,b,x,y,r,theta,L = list(map(int, input().split()))

if (theta == 90 or theta == 270):
  X = x
elif (0 <= theta < 90 or 270 < theta <= 360):
  ref = int((x-r + L * math.cos(math.radians(theta))) / (a - 2*r))
  remain = (x-r + L * math.cos(math.radians(theta))) % (a - 2*r)
  if (ref % 2 == 0):
    X = remain + r
  else:
    X = a - remain - r
else:
  ref = int(((a - x) - L * math.cos(math.radians(theta))) / (a - 2*r))
  remain = ((a - x) - L * math.cos(math.radians(theta))) % (a - 2*r)
  if (ref % 2 == 1):
    X = remain + r
  else:
    X = a - remain - r

if (theta == 0 or theta == 180):
  Y = y
elif (0 <= theta < 180):
  ref = int((y-r + L * math.sin(math.radians(theta))) / (b - 2*r))
  remain = (y-r + L * math.sin(math.radians(theta))) % (b - 2*r)
  if (ref % 2 == 0):
    Y = remain + r
  else:
    Y = b - remain - r
else:
  ref = int(((b - y) - L * math.sin(math.radians(theta))) / (b - 2*r))
  remain = ((b - y) - L * math.sin(math.radians(theta))) % (b - 2*r)
  if (ref % 2 == 1):
    Y = remain + r
  else:
    Y = b - remain - r

print(X, Y)