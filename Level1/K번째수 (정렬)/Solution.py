def solution(array, commands):
  cut_array = [[] for i in range(len(commands))]
  value_array = []

  for i in range(len(commands)):
    cut_array[i] = array[commands[i][0] - 1 : commands[i][1]]
    cut_array[i].sort()
    value_array.append(cut_array[i][commands[i][2] - 1])

  return value_array