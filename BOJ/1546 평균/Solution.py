exam_num = int(input())
bad_score = [0 in range(exam_num)]
bad_score = list(map(int, input().split()))
total_score = 0

high_score = max(bad_score)

for i in range(len(bad_score)):
  bad_score[i] = bad_score[i]/high_score*100
  total_score += bad_score[i]

print(total_score / exam_num)