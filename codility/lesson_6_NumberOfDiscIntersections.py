def solution(A):
    arr = []
    for i,v in enumerate(A):
        arr.append((i+v,1))
        arr.append((i-v,-1))    
    arr.sort()
        
    intersect = 0 # 교차점 갯수
    intervals = 0 # 사이에 있는 것 갯수 
    # -1 나올떄마다 한 depth 씩 깊어지고
    # 1 나올 때마다 한 depth 씩 낮아짐
    for i,v in enumerate(arr):
        if v[1] == -1:
            intersect += intervals
            intervals += 1
        if v[1] == 1:
            intervals -= 1
    if intersect > 10000000:
        return -1
    return intersect