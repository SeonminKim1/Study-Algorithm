def solution(X, A):
    # X => 목표 지점
    # A는 [1,3,1,4,2,3,5,4]
    # K는 시간초
    # A[1]=3 => 1초 때 3번 발판이 준비됨.
    ready = [False]*X
    cnt = 0
    for idx, leaf in enumerate(A):
        if ready[leaf-1]==False:
            ready[leaf-1] = True
            # 멈추는 조건 : 5초면 앞에 1~4초가 완성됬을 때
            # print(leaf, ready)
            cnt+=1
            if cnt == X:
                return idx
    return -1


''' 왜 안되는지 모르겠음 흠
def solution(X, A):
    # X => 목표 지점
    # A는 [1,3,1,4,2,3,5,4]
    # K는 시간초
    # A[1]=3 => 1초 때 3번 발판이 준비됨.
    ready = [False]*X
    for idx, leaf in enumerate(A):
        if ready[leaf-1]==False:
            ready[leaf-1] = True
            # 멈추는 조건 : 5초면 앞에 1~4초가 완성됬을 때
            # print(leaf, ready)
            if all(ready):
                return idx
    return -1
'''