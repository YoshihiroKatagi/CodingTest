N, M = map(int, input().split())
A = list(map(int, input().split()))

A_minus = []
for i in range(N):
  A_minus.append((-1)*A[i])

import heapq

heapq.heapify(A_minus)

for i in range(M):
  X = heapq.heappop(A_minus)
  X/=2
  X = int(X)

  heapq.heappush(A_minus, X)

ans = (-1)*sum(A_minus)
print(ans)