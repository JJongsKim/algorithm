def solution(num):
  answer = 0

  while True:
    if answer == 500:
      return -1
    
    if num == 1:
        return 0

    if num % 2 == 0:
      num = num // 2
      answer += 1
    else:
      num = num * 3 + 1
      answer += 1

    if num == 1:
      break

  return answer