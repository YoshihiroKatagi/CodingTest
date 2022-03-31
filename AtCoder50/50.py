N, M, X, Y = map(int, input().split())

connect = [[] for i in range(N+1)]

for i in range(M):
  A, B, T, K = map(int, input().split())
  connect[A].append([B, T, K])
  connect[B].append([A, T, K])

que = list()

import heapq
heapq.heappush(que, [0, X])

time = [10**20] * (N+1)
time[X] = 0
confirmed = [False] * (N+1)

from math import ceil

while 0<len(que):
  now_time, now_place = heapq.heappop(que)

  if confirmed[now_place]==True:
    continue
  
  confirmed[now_place] = True

  for to_place, T, K in connect[now_place]:
    if confirmed[to_place]==False:
      to_time = ceil(now_time/K) * K + T
      if to_time<time[to_place]:
        time[to_place] = to_time
        heapq.heappush(que, [to_time, to_place])

if time[Y]==10**20:
  print(-1)
else:
  print(time[Y])