S = input()
N = len(S)
S_ = []

for s in S:
  S_.append(s)

Char_dict = {
  'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0,
  'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0,
  'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0
}


def is_int(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

#文字列連続に1
j = 0
if is_int(S[0])==False:
  S_.insert(0,'1')
  j+=1
for i in range(1,N):
  if is_int(S[i])==False:
    if is_int(S[i-1])==False:
      if S[i]!=')':
        S_.insert(i+j,'1')
        j+=1


flag = 0
Num_=[0 for _ in range(1000)]
for s in S_:
  if is_int(s):
    Num_[flag] = 10 * Num_[flag] + int(s)
  if is_int(s)==False:
    if s == '(':
      flag+=1
    if s == ')':
      flag-=1
      Num_[flag]=0
    if s!='(' and s!=')':
      Num = 1
      for i in range(flag+1):
        Num *= Num_[i]
      Char_dict[s] += Num
      Num_[flag]=0

for key, value in Char_dict.items():
  print(key + ' ' + str(value))