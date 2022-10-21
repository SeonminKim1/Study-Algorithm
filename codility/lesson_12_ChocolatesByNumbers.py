from math import gcd

# 공약수 구해서 나누기
def solution(N, M):
    return N//gcd(M,N)

## Timeout O(N+M)
def solution(N, M):
    start = 0
    result_list = [0]
    while True:
        start = (start+M) % N

        if start not in result_list:
            result_list.append(start)
        else:
            break
    return len(result_list)