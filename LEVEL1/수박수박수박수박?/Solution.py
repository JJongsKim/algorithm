def solution(n):
  text = '수박'

  if n % 2 == 0:
    answer = text * (n // 2)
  else:
    answer = text * (n // 2) + '수'

  return answer