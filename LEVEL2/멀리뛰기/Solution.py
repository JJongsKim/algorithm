def solution(n):
    answer = 0
    st = dict()
    st[0] = 1
    st[1] = 1

    for i in range(2, n+1):
        st[i] = st[i-1] + st[i-2]

    return st[n] % 1234567