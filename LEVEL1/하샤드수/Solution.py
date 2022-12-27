def solution(x):
  num_sum = 0 

  ex = list(str(x))
  ex = list(map(int, ex))

  for i in range(len(ex)):
    num_sum += ex[i]

  if (x % num_sum == 0):
    return True
  else:
    return False
