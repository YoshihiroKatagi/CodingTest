N, M = map(int, input().split())

connect = [[] for i in range(N+1)]

for i in range(M):
  A, B = map(int, input().split())
  connect[A].append(B)
  connect[B].append(A)

visited = [False]*(N+1)
visited[1] = True

from collections import deque
que = deque()
que.append(1)

ans = [0]*(N+1)

while 0<len(que):
  now_room = que.popleft()

  for to_room in connect[now_room]:
    if visited[to_room]==False:
      visited[to_room] = True

      ans[to_room] = now_room
      que.append(to_room)

print(connect)
print("Yes")
for i in range(2, N+1):
  print(ans[i])