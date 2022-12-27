def solution(n):
  answer = ""
  ex = list(str(n))
  ex.sort(reverse=True)

  for i in range(len(ex)):
    answer += ex[i]

  answer = int(answer)

  return answer