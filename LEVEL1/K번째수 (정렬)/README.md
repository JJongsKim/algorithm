## K번째 수 (정렬문제)

### 문제설명

배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

1. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
2. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
3. 2에서 나온 배열의 3번째 숫자는 5입니다.

배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

### 제한조건

- array의 길이는 1 이상 100 이하입니다.
- array의 각 원소는 1 이상 100 이하입니다.
- commands의 길이는 1 이상 50 이하입니다.
- commands의 각 원소는 길이가 3입니다.

### 입출력 예

| x                     | n                                 | return    |
| --------------------- | --------------------------------- | --------- |
| [1, 5, 2, 6, 3, 7, 4] | [[2, 5, 3], [4, 4, 1], [1, 7, 3]] | [5, 6, 3] |

## 🔥 내 풀이

풀이를 뒤늦게 작성하면서 내가 풀었던 문제가 이해되지 않아 오래생각했다🤣.  
다음번 이 README를 읽을 땐 바로 이해할 수 있도록 바로 정리해보자면,  
[2, 5, 3]은 i = 2 j = 5 k = 3 / [4, 4, 1]은 i = 4 j = 4 k = 1 / [1, 7, 3]은 i = 1 j = 7 k = 3 으로 commands의 각 배열에 주어진 수대로 구해야하는 것이었다.

그렇게 풀기 위해선 주어진 commands를 배열마다 나누는 작업이 필요했다.  
그래서 cut_array 라는 변수를 하나 만들어 commands의 길이를 가진 중첩배열 하나를 만들어준다.  
cut_array는 우선 [[], [], []]형태를 갖게 된다!

그 다음 commands에 대해 for문을 돌린다.

- commands의 각 배열에 대해 구해야 하는 것이므로 구할 때도 commands에는 이중배열 작성법을 사용해야 한다.
- commands의 n번째 배열에서 i, j 값을 이용해 배열 array를 잘라준다. (이때 잘라야 하는 array에 인덱스가 적용되기 때문에 - 1을 붙여야 한다)
- 해당 자른 배열을 오름차순 정렬해준다.
- return 값만을 담을 변수를 하나 만들어 append() 함수로 원하는 출력값만 담는다.

이때 return에 들어가야 할 값들은 array에서 commands배열의 마지막 숫자 자리 값 이므로  
cut_array[i]commands[i][2] - 1]를 통해 구해줄 수 있다.

```python
def solution(array, commands):
  cut_array = [[] for i in range(len(commands))]
  value_array = []

  for i in range(len(commands)):
    cut_array[i] = array[commands[i][0] - 1 : commands[i][1]] # -1 을 안 해줄 경우, array를 잘랐을 때 원하는 자릿수 + 1이 되어버린다.
    cut_array[i].sort()
    value_array.append(cut_array[i][commands[i][2] - 1]) # 여기도 마찬가지로 array기준으로 -1을 해줘야 한다.

  return value_array
```
