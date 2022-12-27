def solution(n, lost, reserve): # 전체 학생의 수, 도난 당한 학생의 수 배열, 여벌 체육복 있는 학생 번호 배열
    answer = 0
    reserve_new = set(reserve) - set(lost)
    lost_new = set(lost) - set(reserve)
    
    for i in reserve_new:
        if i-1 in lost_new:
            lost_new.remove(i - 1)
        elif i+1 in lost_new:
            lost_new.remove(i + 1)
    
    answer = n - len(lost_new)
    return answer