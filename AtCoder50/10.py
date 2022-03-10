def Divisor_List(N):
  divisor = []
  i=1
  while i**2<=N:
    if N%i==0:
      divisor.append(i)
      if i!=N//i:
        divisor.append(N//i)
    i+=1

  divisor.sort()
  return divisor

N = int(input())

ans = Divisor_List(N)

for x in ans:
  print(x)