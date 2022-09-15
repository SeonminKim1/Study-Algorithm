def solution(arr, divisor):
    ls = sorted([i for i in arr if i%divisor==0])
    return [-1] if len(ls)==0 else ls

    ## if-else 문 한줄로
    # if len(ls)==0:
    #     return [-1]
    # else: 
    #     return ls