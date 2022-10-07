def solution(A):
    max_num, len_num = max(A), len(A)
    if len(set(A)) != len(A):
        return 0
    elif len_num == max_num:
        return 1
    else:
        return 0