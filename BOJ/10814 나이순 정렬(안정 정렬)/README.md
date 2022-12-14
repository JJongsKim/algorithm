## 10814 나이순 정렬 (안정 정렬)

### 문제

온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

### 입력

첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다.  
나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다.  
입력은 가입한 순서로 주어진다.

### 출력

첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

## 🔥 내 풀이

해당 문제는 나이와 이름을 모두 입력받아서 sort()로 처리할 수 없는 문제였다.  
그 이유는 나이가 같더라도 이름 순서에 따라 늦게 가입한 사람이 먼저 정렬되는 문제가 있었기 때문이다.

내 풀이에서 핵심은 배열에 정보를 추가할 때, 나이와 이름 뿐만 아니라 그 사이에 입력된 순서가 들어갈 수 있도록 넣어서 이름 순서가 늦더라도 먼저 가입한 사람이라면 먼저 출력할 수 있도록 만들었다.  

![스크린샷 2022-12-27 오후 7 11 24](https://user-images.githubusercontent.com/81777778/209668041-333201bd-7981-48e0-a293-9d680b413367.png)

```python
import sys

user_num = int(sys.stdin.readline())
user = []

for i in range(user_num):
  age, name = map(str, sys.stdin.readline().split())
  user.append([int(age), i, name]) # 여기서 i 가 핵심이다!

user.sort()

for j in range(len(user)):
  print(user[j][0], user[j][2])
```
