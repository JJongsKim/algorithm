def solution(s):
  texts = s.split(' ')
  answer = ''

  for text in texts:
    for i in range(len(text)):
      if i % 2 == 0:
        answer += text[i].upper()
      else:
        answer += text[i].lower()
    answer += ''

  return answer[:-1]