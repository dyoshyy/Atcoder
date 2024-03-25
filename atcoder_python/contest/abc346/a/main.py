N = int(input())

A = input().split()
B = []
for i in range(N-1):
  B.append(int(A[i])*int(A[i+1]))
  
print(' '.join(map(str, B)))