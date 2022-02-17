import math

H, W = map(int, input().split(' '))
h_0, w_0 = map(int, input().split(' '))
town = []
for h in range(H):
  t_w = input()
  town.append(t_w)

rich_map = []
for h in range(H):
  r_m = []
  for w in range(W):
    if town[h][w] == '*':
      r_m.append(1)
    else:
      r_m.append(0)
  rich_map.append(r_m)

mouse_h = h_0 - 1
mouse_w = w_0 - 1
X = 3
def dir_h(x):
  return int(math.sin(math.pi / 2 * x))
def dir_w(x):
  return int(math.cos(math.pi / 2 * x))

while 0 <= mouse_h < H and 0 <= mouse_w < W:
  if rich_map[mouse_h][mouse_w] == 0:
    rich_map[mouse_h][mouse_w] = 1
    X += 1
    mouse_h += 1 * dir_h(X)
    mouse_w += 1 * dir_w(X)
  else:
    rich_map[mouse_h][mouse_w] = 0
    X -= 1
    mouse_h += 1 * dir_h(X)
    mouse_w += 1 * dir_w(X)

new_map = []
for h in range(H):
  n_m = []
  for w in range(W):
    if rich_map[h][w] == 0:
      n_m.append('.')
    else:
      n_m.append('*')
  n_m = ''.join(n_m)
  new_map.append(n_m)

for h in range(H):
  print(new_map[h])

#result... timeover(予定がなければできてた)