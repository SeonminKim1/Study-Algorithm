def solution(A):
    full_list = range(1, len(A)+2)
    return list(set(full_list) - set(A))[0]
