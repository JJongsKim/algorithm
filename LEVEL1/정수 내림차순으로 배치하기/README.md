## 정수 내림차순으로 배치하기

### 문제설명

함수 solution은 정수 n을 매개변수로 입력받습니다.  
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.  
예를들어 n이 118372면 873211을 리턴하면 됩니다.

### 제한조건

- n은 1이상 8000000000 이하인 자연수입니다.

### 입출력 예

| n      | return |
| ------ | ------ |
| 118372 | 873211 |

## 🔥 내 풀이

해당 문제는 자연수 뒤집어 배열 만들기 문제와 비슷하게 풀었다!  
[자연수 뒤집어 배열 만들기](https://github.com/JJongsKim/algorithm/tree/main/Level1/%EC%9E%90%EC%97%B0%EC%88%98%20%EB%92%A4%EC%A7%91%EC%96%B4%20%EB%B0%B0%EC%97%B4%EB%A1%9C%20%EB%A7%8C%EB%93%A4%EA%B8%B0)

우선 들어온 숫자를 str()로 문자열로 만든 후 list()로 문자열 배열로 만들어준다.  
그리고 문자열을 큰 것부터 작은 순으로 정렬하기 위해 .sort(reverse=True)를 해주었다.  
그냥 .sort()만 줄 경우 오름차순 정렬이 되어버린다(작은 수에서 큰 수로..)

해당 문자 배열을 반복문을 통해 빈 값이었던 answer에 하나씩 담아준다.  
그럼 answer은 "8" + "7" + "3" + ...와 같이 "873211" 이라는 값을 갖게 된다.  
이 문자열을 바로 숫자 정수형으로 바꾸어주면, 원하는 return 값을 얻을 수 있다!

```python
  def solution(n):
  answer = ""
  ex = list(str(n))
  ex.sort(reverse=True)

  for i in range(len(ex)):
    answer += ex[i]

  answer = int(answer)

  return answer
```
