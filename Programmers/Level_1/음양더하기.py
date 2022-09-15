def solution(absolutes, signs):
    sum = 0
    for i, j in zip(absolutes, signs):
        j = '+' if j else '-'
        sum += int(j + str(i))
    return sum