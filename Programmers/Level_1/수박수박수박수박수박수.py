def solution(n):
    ## case 1
    '''
    if n%2==0:
        return "수박" * int(n/2)
    else:
        return "수박" * int(n/2) + '수'
    '''
    
    ## case 2
    s = "수박" * n
    return s[:n]