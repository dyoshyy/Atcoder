N = int(input())
T = input()

if N % 2 == 0:
  print("No")
  exit()

for i in range(N):
    if i < N // 2:
        if T[i] == '1':
            continue
        else:
            print("No")
            exit()
    elif i == N // 2:
        if T[i] == '/':
            continue
        else:
            print("No")
            exit()
    else:
        if T[i] == '2':
            continue
        else:
            print("No")
            exit()

print("Yes")
    