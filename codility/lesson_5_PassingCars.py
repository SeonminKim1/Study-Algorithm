# O(N^2)
def solution(A):
    count_sum = 0
    for idx, num in enumerate(A):
        if num==0:
            count_sum += A[idx:].count(1)

    if count_sum > 1000000000:
        return -1
    else:
        return count_sum

# ======= 
# O(N) - 진짜 정답
def solution(A):
    count_sum = 0
    zero_num = 0
    for num in A[::-1]:
        if num==1:
            zero_num += 1
        else:
            count_sum += zero_num
    if count_sum > 1000000000:
        return -1
    else:
        return count_sum