Y = int(input())

if Y==0:
  print([])

if Y==1:
  print([1])

import itertools

for i in range(1, 10**5+10):
  for seq in itertools.product([0,1], repeat=i):
    total=0
    for j in range(i):
      total += seq[j] * (-2)**j
    total += 1 * (-2)**i

    if total==Y:
      seq+=(1,)
      print(seq)
      exit()
