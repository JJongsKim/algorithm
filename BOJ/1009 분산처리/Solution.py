import sys

test_num = int(sys.stdin.readline())
# 제곱의 규칙 구하기
result_array = [[0], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6, 4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1, 9, 1]]

for _ in range(test_num):
    a, b = map(int, sys.stdin.readline().split())
    
    # a의 일의 자리가 0일때
    if a % 10 == 0:
        print(10)
        continue
    # a의 일의 자리가 1, 5, 6일 땐, 결과도 그대로 출력
    elif a % 10 == 1 or a % 10 == 5 or a % 10 == 6:
        print(a % 10)
        continue
    
    # 제곱하는 b가 0일땐 값도 무조건 1
    if b == 0:
        print(1)
    # 제곱하는 b도 4번의 제곱규칙 적용으로 % 4를 해준다
    elif b % 4 == 0:
        print(result_array[a % 10][3])
    else:
        print(result_array[a % 10][b % 4 - 1])