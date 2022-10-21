def solution(A):
    A.sort()
    # [1,2,3,4,6]
    min_value = 1
    for i in A:
        if i==min_value:
            min_value += 1
    return min_value