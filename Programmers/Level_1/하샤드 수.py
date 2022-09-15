def solution(x):
    # case 1
    '''
    num = sum([int(i) for i in str(x)]) # 자릿수의 합
    if x%num==0:
        return True 
    else:
        return False
    '''
    return x % sum([int(c) for c in str(x)]) == 0 # 자동으로 True, False...

    