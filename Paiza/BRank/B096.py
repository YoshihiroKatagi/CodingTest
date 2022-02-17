H, W = map(int, input().split(' '))
fields = []
for h in range(H):
  w_field = input()
  fields.append(w_field)

bomb_fields = []
for h in range(H):
  bomb_f = []
  for w in range(W):
    bomb_f.append(0)
  bomb_fields.append(bomb_f)

# print(bomb_fields)

count = 0
for h in range(H):
  for w in range(W):
    if fields[h][w] == '#':
      for w_b in range(W):
        bomb_fields[h][w_b] = 1
      for h_b in range(H):
        bomb_fields[h_b][w] = 1

for h in range(H):
  for w in range(W):
    if bomb_fields[h][w] == 1:
      count += 1

print(count)

#result... all clear