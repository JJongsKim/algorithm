## 11047 동전0 (그리디)

### 문제

준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

### 입력

첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

### 출력

첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

## 🔥 내 풀이

우선 풀이를 위해서 리턴될 값, 동전의 종류, 얼마인지 받을 변수를 만들어 세팅해둔다.
그 다음 동전의 종류가 들어갈 배열을 동전의 종류 수 만큼 미리 만들어놓는다.

동전의 종류를 큰 순서대로 정렬하기 위해 .sort(reverse=True)를 해주었다.

그 다음 동전의 종류만큼 반복문을 돌리며 돈이 동전의 종류보다 클수록(4200원이라고 했을 때 5000원이 아닌 1000원으로 나눠 4개의 지폐로 받아갈 수 있다는 느낌처럼)
리턴할 값 answer에 money를 동전의 종류 coin으로 나눈값을 우선 더한다.

그리고 money는 coin으로 나눈 **나머지의 값**으로 값을 바꿔준다.  
예를 들어 4200원을 1000원 4개로 우선 바꿔가고, 4200 % 1000 = 200 이므로 200에서 coin 반복문을 돌려야하기 때문이다!

이 반복문을 돌려가며 money가 0이 될 시 반복문을 탈출하는 break를 걸어주면 된다.

```python
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
```
