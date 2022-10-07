
def solution(A):
    # 구해야 하는 것 특정 INDEX 기준 앞에값 - 뒤에값
    # [3,1,2,4,3]
    diff = []
    scope1 = 0
    scope2 = sum(A)
    for val in A:
        scope1 +=val
        scope2 -=val
        diff.append(abs(scope1-scope2))

    return min(diff[:-1])