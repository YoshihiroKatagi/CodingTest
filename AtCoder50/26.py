S = input()
Q = int(input())

inv = False

from collections import deque
S_deque = deque()

for i in range(len(S)):
  S_deque.append(S[i])

for i in range(Q):
  TFC = list(map(str, input().split()))

  if TFC[0]=="1":
    if inv==False:
      inv=True
    else:
      inv=False
  
  else:
    F=TFC[1]
    C=TFC[2]

    if inv==False:
      if F=="1":
        S_deque.appendleft(C)
      else:
        S_deque.append(C)
    else:
      if F=="1":
        S_deque.append(C)
      else:
        S_deque.appendleft(C)

ans = "".join(S_deque)

if inv==True:
  ans = ans[::-1]

print(ans)