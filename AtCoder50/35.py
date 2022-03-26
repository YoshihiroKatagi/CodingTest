def price(N):
  N_str = str(N)
  d = len(N_str)
  return A*N + B*d

A, B, X = map(int, input().split())

if X<price(1):
  price(0)
  exit()

left = 1
right = 10**20

while 1<right-left:
  N = (left + right) // 2
  if price(N)<=X:
    left = N
  else:
    right = N

if 10**9<left:
  left = 10**9
print(left)