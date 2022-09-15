def solution(arr):
    ## case 1
    arr.remove(min(arr))
    if len(arr)==0:
        return [-1]
    return arr

    ## case 2 - 만약 가장 작은 min 값이 여러번 들어 있으면 아래 코드가 맞음
    '''
    mininum = min(arr)
    ls = [i for i in arr if i!=mininum]
    if len(ls)==0:
        return [-1]
    else:
        return ls
    '''