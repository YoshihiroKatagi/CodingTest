# A, B = map(int, input().split())

# N = max(A, B)
# ans=1
# for i in range(1, N):
#   if A%i==0 and B%i==0:
#     ans*=i
#     A//=i
#     B//=i

# ans = ans * A * B

# print(ans)


import math
def lcm(x,y):
  return (x*y)//math.gcd(x,y)

A, B = map(int, input().split())
print(lcm(A, B))