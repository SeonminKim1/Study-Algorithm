def solution(arr):
    # case 1
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

    ## case 2
    # answer = []
    # for i in arr:
    #     if answer[-1:] == [i]: continue
    #     answer.append(i)
    # return answer
