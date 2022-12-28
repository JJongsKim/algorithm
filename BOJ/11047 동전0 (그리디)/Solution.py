import sys

answer = 0
kinds, money = map(int, sys.stdin.readline().split())
coins = [0 for i in range(kinds)]

for i in range(kinds):
  coins[i] = int(sys.stdin.readline())

coins.sort(reverse=True)

for coin in coins:
  if money >= coin:
    answer += (money // coin)
    money %= coin

    if money <= 0:
      break

print(answer)