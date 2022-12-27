## 10989 수 정렬하기3

### 문제

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

### 입력

첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

### 출력

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

## 🔥 내 풀이

해당 문제는 일반적인 숫자 정렬과 다르게 메모리 제한이 굉장히 작은 문제였다.  
그래서 코드제출 시 계속해서 메모리 초과가 나와서 실패했고, 결국엔 검색의 힘을 빌린 문제이기도 했다.

이 문제의 핵심은 **10,000보다 작거나 같은 자연수**라는 것에 초점을 두고 풀면 되는 문제였다.

🥲 메모리 초과 코드

```python
import sys

num = int(sys.stdin.readline())
num_array = [0 for i in range(num)]
answer = ""

for i in range(len(num_array)):
  num_array[i] = int(sys.stdin.readline())

num_array.sort()

for j in range(len(num_array)):
    print(num_array[j])
```

우선 몇 개의 수를 입력받을 것인지 결정할 수를 입력받는다.  
그리고 개수는 10000 이하가 될 것이므로 미리 인덱스를 고려한 10001 배열을 만들어 놓는다.

그리고 입력받은 num 횟수만큼 반복하며 수를 받고, 그 수를 배열의 인덱스에 넣어 입력 받은 수 인덱스 위치에 1을 새롭게 넣어준다.

그리고 10001 배열을 반복문으로 돌려 입력 받은 수 인덱스 숫자를 출력해주면 되는 것이다.

이렇게 메모리 제한이 굉장히 작은 문제에서는 평소에 써왔던 sort() 함수를 쓸 시 메모리 초과가 나오는 것 같다.  
주의하여 문제를 풀 필요가 있다!

💛 제출 성공한 코드!!

```python
import sys

num = int(sys.stdin.readline())
num_array = [0] * 10001

for i in range(num):
    data = int(sys.stdin.readline())
    num_array[data] += 1 # 입력 받은 수 인덱스 위치에만 1로 새롭게 넣어주기

for j in range(len(num_array)):
    if num_array[j] != 0:
        for _ in range(num_array[j]):
            print(j)
```
