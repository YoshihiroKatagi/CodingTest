N, K = map(int, input().split())
p = list(map(int, input().split()))

p_ex = []
for i in range(N):
  p_ex.append((p[i]+1)/2)

p_ex_Cum = [p_ex[0]]
for i in range(1, N):
  p_ex_Cum.append(p_ex_Cum[i-1]+p_ex[i])

ans = -10**15
for i in range(N-K+1):
  if i==0:
    ans_tmp = p_ex_Cum[i+K-1]
  else:
    ans_tmp = p_ex_Cum[i+K-1] - p_ex_Cum[i-1]
  
  ans = max(ans, ans_tmp)

print(ans)