def solution(arr1, arr2):
    ## case 1
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    return arr1

    
    ## case 2
    '''
    answer = [[a+b for a, b in zip(i, j)] for i, j in zip(arr1, arr2)]
    return answer
    '''