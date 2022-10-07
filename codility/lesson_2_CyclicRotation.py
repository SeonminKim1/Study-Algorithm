def solution(A, K):
    list_length = len(A)
    
    result = [0]*list_length
    for idx, n in enumerate(A):
        result[(idx+K)%list_length] = n

    return result