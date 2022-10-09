def solution(A):
    A = sorted(A)
    
    # 1, 2, 5, 8, 10, 20 이라고 가정
    for i in range(len(A)-2):
        # 조건 
        # 1) a+b > c => 확인 필요
        # 2) a+c > b => 정렬하면 c가 b보다 크므로 확인 불필요
        # 3) b+c > a => 정렬하면 c가 a보다 크므로 확인 불필요
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0
