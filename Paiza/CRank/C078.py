N, min_p, max_p = map(int, input().split(' '))

stock_p = []
for i in range(N):
  stock = int(input())
  stock_p.append(stock)
# print(stock_p)

stock_n = 0
benefit = 0

for i in range(N):
  if i+1 != N:
    if stock_p[i] <= min_p:
      benefit -= stock_p[i]
      stock_n += 1
    elif stock_p[i] >= max_p:
      benefit += stock_p[i] * stock_n
      stock_n = 0
  else:
    benefit += stock_p[i] * stock_n
    stock_n = 0

print(benefit)