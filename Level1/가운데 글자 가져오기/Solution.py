def solution(s):
  slice_num = (len(s) // 2)
  
  if (len(s) % 2 == 0):
    answer = s[slice_num-1:slice_num+1]
  else:
    answer = s[slice_num]

  return answer