H, W = map(int, input().split())

maze = []
for i in range(H):
  tmp = input()
  maze.append(list(tmp))

from collections import deque

def explore(start_gyou, start_retu):
  maze_count = [[-1]*W for i in range(H)]
  maze_count[start_gyou][start_retu] = 0

  que = deque()
  que.append([start_gyou, start_retu])

  while 0<len(que):
    now_gyou, now_retu = que.popleft()
    now_count = maze_count[now_gyou][now_retu]

    if 0<=now_gyou-1<H and 0<=now_retu<W:
      if maze[now_gyou - 1][now_retu] == ".":
        if maze_count[now_gyou - 1][now_retu] == -1:
          maze_count[now_gyou -1][now_retu] = now_count+1
          que.append([now_gyou -1, now_retu])

    if 0<=now_gyou+1<H and 0<=now_retu<W:
      if maze[now_gyou + 1][now_retu] == ".":
        if maze_count[now_gyou + 1][now_retu] == -1:
          maze_count[now_gyou + 1][now_retu] = now_count+1
          que.append([now_gyou + 1, now_retu])

    if 0<=now_gyou<H and 0<=now_retu-1<W:
      if maze[now_gyou][now_retu - 1] == ".":
        if maze_count[now_gyou][now_retu - 1] == -1:
          maze_count[now_gyou][now_retu - 1] = now_count+1
          que.append([now_gyou, now_retu - 1])

    if 0<=now_gyou<H and 0<=now_retu+1<W:
      if maze[now_gyou][now_retu + 1] == ".":
        if maze_count[now_gyou][now_retu + 1] == -1:
          maze_count[now_gyou][now_retu + 1] = now_count+1
          que.append([now_gyou, now_retu + 1])

  max_count = 0
  for gyou in range(H):
    for retu in range(W):
      max_count = max(max_count, maze_count[gyou][retu])
  
  return max_count

ans = 0
for gyou in range(H):
  for retu in range(W):
    if maze[gyou][retu]==".":
      ans = max(ans, explore(gyou, retu))

print(ans)