import sys

user_num = int(sys.stdin.readline())
user = []

for i in range(user_num):
  age, name = map(str, sys.stdin.readline().split())
  user.append([int(age), i, name])

user.sort()

for j in range(len(user)):
  print(user[j][0], user[j][2])