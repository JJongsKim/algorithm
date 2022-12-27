sugar = int(input())
count = 0

while (True):
    if sugar % 5 == 0:
        count += (sugar // 5)
        break
    else:
        # 설탕이 딱 떨어지지 못할 때,
        if sugar < 3:
            count = -1
        sugar -= 3
        count += 1
        
print(count)