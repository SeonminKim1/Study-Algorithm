# 중첩 여부 판단
def solution(S):
    str_list = []
    for i in S:
        if i == '(':
            str_list.append(i)
        else:
            # ( 가 없었다는 것
            if len(str_list)==0: return 0
            elif i== ')':
                str_list.pop()
            else:
                return 0
    if len(str_list)==0:
        return 1
    else:
        return 0