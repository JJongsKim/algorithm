## 이상한 문자 만들기

### 문제설명

문자열 s는 한 개 이상의 단어로 구성되어 있습니다.  
각 단어는 하나 이상의 공백문자로 구분되어 있습니다.  
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

### 제한사항

- 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
- 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

### 입출력 예

| s                 | return            |
| ----------------- | ----------------- |
| "try hello world" | "TrY HeLlO WoRlD" |

### 입출력 예 설명

"try hello world"는 세 단어 "try", "hello", "world"로 구성되어 있습니다.  
각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 "TrY", "HeLlO", "WoRlD"입니다.  
따라서 "TrY HeLlO WoRlD" 를 리턴합니다.

## 🔥 내 풀이

```python
def solution(s):
  texts = s.split(' ') # 들어온 문자열을 공백에 따라 분류해준다
  answer = '' # 새로운 문자열을 받을 수 있는 변수 추가

  for text in texts: # 공백에 따라 분류시킨 문자열을, 해당 문자마다 반복문을 돌려준다. 첫 번째 반복문은 try기준, 두 번째 반복문은 hello, 기준 세 번째 반복문은 world 기준
    for i in range(len(text)):
      if i % 2 == 0:
        answer += text[i].upper()
      else:
        answer += text[i].lower()
    answer += '' # 대문자 소문자 변경이 된 문자열들을 answer에 모두 합쳐준다

  return answer[:-1] # answer 마지막에 입력된 공백을 제외한 값으로 return 해야하므로 [:-1]을 넣었다!
```
