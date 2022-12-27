def solution(n):
  value = n ** 0.5
  value = int(value)

  if value * value == n:
    answer = value + 1
    answer *= answer

  else:
    answer = -1

  return answer