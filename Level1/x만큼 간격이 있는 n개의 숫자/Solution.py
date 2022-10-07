def solution(x, n):
  origin_num = x;
  answer = [0 for i in range(n)]
  answer[0] = x

  for i in range(n):
    if i + 1 < n:
      x += origin_num
      answer[i + 1] = x

  return answer