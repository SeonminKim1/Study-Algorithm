def solution(numbers):
    ## case 1
    return sum(set(range(0, 10)) - set(numbers))

    ## case 2
    # return 45 - sum(numbers)