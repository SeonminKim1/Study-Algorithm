def solution(a, b):
    ## case 1
    # if b>=a:
    #     return sum([i for i in range(a, b+1)])
    # else:
    #     return sum([i for i in range(b, a+1)])
    
    ## case 2
    if a > b: # b가 무조건 크다고 가정
        a, b = b, a
    return sum(range(a,b+1))