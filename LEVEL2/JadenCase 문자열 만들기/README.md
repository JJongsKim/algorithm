## JadenCase 문자열 만들기

### 문제설명

JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.  
단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)  
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

### 제한조건

- s는 길이 1 이상 200 이하인 문자열입니다.
- s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
  - 숫자는 단어의 첫 문자로만 나옵니다.
  - 숫자로만 이루어진 단어는 없습니다.
  - 공백문자가 연속해서 나올 수 있습니다.

### 입출력 예

| s                       | return                  |
| ----------------------- | ----------------------- |
| "3people unFollowed me" | "3people Unfollowed Me" |
| "for the last week"     | "For The Last Week"     |

## 🔥 내 풀이

처음 문제 풀이는 아래와 같이 풀었으나, 공백이 여러개일수도 있다는 조건 때문에  
주어진 단어의 공백이 2개 이상이더라도 내가 짠 코드는 문자열을 합칠 때 공백이 하나로만 되어버리는 현상이 발생해서 몇몇 테스트케이스에서 오류가 떠버렸다.  

<img width="818" alt="스크린샷 2022-12-11 오후 4 49 37" src="https://user-images.githubusercontent.com/81777778/206893268-90d21489-9927-4b0e-896d-55c54a14542c.png">
```python
def solution(s):
    texts = s.split()
    answer = ""

    for text in texts:
        for i in range(len(text)):
            if i == 0:
                answer += text[i].upper()
            else:
                answer += text[i].lower()
        answer += " "

    return answer[:-1]
```

여기서 실수했던 점은 split()을 사용하면서 추가적인 공백이 있을 땐 (" ")을 써줄 때 추가 공백이 적용이 되는데, 이를 빼먹었기 때문에 여러 테스트케이스에서 오류가 떴던 것이었다.  
그래서 재수정 후 다시 코드를 돌렸고 오류없이 통과된 것을 확인할 수 있었다.

```python
def solution(s):
    answer = ""
    texts = s.split(" ") # 이 부분!!!!!

    for text in texts:
        for i in range(len(text)):
            if i == 0:
                answer += text[i].upper()
            else:
                answer += text[i].lower()
        answer += " "

    return answer[:-1]
```

혹은 가장 편안한 방법으로 앞글자만 대문자로 변환해줄 수 있는 파이썬의 내장함수를 발견했다.  
바로 .capitalize() 함수를 사용하면 되는 것이었다 ..!!

```python
def solution(s):
    answer = ""
    texts = s.split(" ")

    for i in range(len(texts)):
        texts[i] = texts[i].capitalize()

    answer = ' '.join(texts)

    return answer
```
