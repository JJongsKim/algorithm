## 핸드폰 번호 가리기

### 문제설명

프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.  
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 \*으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

### 제한조건

- phone_number는 길이 4 이상, 20이하인 문자열입니다.

### 입출력 예

| PHONE_NUMBER  | return           |
| ------------- | ---------------- |
| "01033334444" | "**\*\*\***4444" |
| "027778888"   | "**\***8888"     |

## 🔥 내 풀이

전화번호 길이의 변화가 있더라도 전화번호 끝 4자리는 변함이 없기 때문에 이를 이용했다.  
len(phone_number) - 4를 이용해 가려야하는 앞자리 문자열을 변수에 담아준다.  
그 다음 phone_number의 문자열을 변경하기 위해 replace() 함수를 이용해 가려야하는 숫자를 \*로 변경해주었다.

```python
def solution(phone_number):
  text = phone_number[:len(phone_number)-4] # 가려야하는 문자열을 담을 text 변수 만들기
  answer = phone_number.replace(text, "*"*len(text)) # 원래 문자열에 replace 적용, 가려야하는 문자열인 text를 적용해준다.

  return answer
```
