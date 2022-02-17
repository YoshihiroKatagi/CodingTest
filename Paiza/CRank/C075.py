N, M = map(int, input().split(' '))
wages = []
for i in range(M):
  wage = int(input())
  wages.append(wage)

# print(wages)

p = 0
for i in range(M):
  if p < wages[i]:
    N -= wages[i]
    p += wages[i] // 10
    print(N, p)
  else:
    p -= wages[i]
    print(N, p)


# result...test case 3 failed