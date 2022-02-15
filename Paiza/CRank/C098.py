N = int(input())
ball_nums = []
for i in range(N):
  num = int(input())
  ball_nums.append(num)

# print(ball_nums)

M = int(input())
actions = []
for i in range(M):
  action = list(map(int, input().split(' ')))
  actions.append(action)

# print(actions)

for i in range(M):
  if actions[i][2] <= ball_nums[actions[i][0]-1]:
    ball_nums[actions[i][0]-1] -= actions[i][2]
    ball_nums[actions[i][1]-1] += actions[i][2]
  else:
    ball_nums[actions[i][1]-1] += ball_nums[actions[i][0]-1]
    ball_nums[actions[i][0]-1] = 0

for i in range(N):
  print(ball_nums[i])