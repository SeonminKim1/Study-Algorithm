# A = [3,2,-6,4,0]
def solution(A):
    # 음수가 나오기 전까지 계속 합을 더해줌
    # 음수가 나오면 다시 누적합을 구하기 시작함
    
    max_sum = -1000000
    max_part_sum = 0

    for n in A:
        max_sum = max(max_sum, max_part_sum + n)
        max_part_sum = max(0, max_part_sum + n)
    return max_sum

def solution(A):
    max_sum = -1000000
    max_part_sum = 0
    for n in A:
        max_sum = max(max_sum, max_part_sum+n)
        max_part_sum = max(0, max_part_sum+n)