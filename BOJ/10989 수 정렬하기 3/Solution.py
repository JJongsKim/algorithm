import sys

num = int(sys.stdin.readline())
num_array = [0] * 10001

for i in range(num):
    data = int(sys.stdin.readline())
    num_array[data] += 1 # 입력 받은 수 인덱스 위치에만 1로 새롭게 넣어주기
    
for j in range(len(num_array)):
    if num_array[j] != 0:
        for _ in range(num_array[j]):
            print(j)