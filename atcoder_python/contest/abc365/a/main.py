Y = int(input())

if Y % 4 == 0:
  if Y % 100 != 0:
    print("366")
    exit()
  elif Y % 400 != 0:
    print("365")
    exit()
  else:
    print("366")
    exit()
else:
  print("365")
    