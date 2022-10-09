def solution(S):
    check_dict = {
        '(':1, ')':-1,
        '{':2, '}':-2,
        '[':3, ']':-3,
    }
    str_list = []
    for word in S:
        if word in '{[(':
            str_list.append(word)
        elif word in ')]}':
            if str_list == []: return 0 # 잘못 들어왔을 때 ex) ')[]()
            word_f = str_list.pop()
            if check_dict[word_f] != -int((check_dict[word])):
                return 0
    if len(str_list)==0:
        return 1
    else:
        return 0

# ===== 구버전 코드 (75%)
def solution(S):
    while True:
        f1 = S.find('()')
        f2 = S.find('{}')
        f3 = S.find("[]")
        if f1 != -1:
            S = S.replace('()','')
        if f2 != -1:
            S = S.replace('{}','')
        if f3 != -1:
            S = S.replace('[]','')
        if f1==-1 and f2==-1 and f3==-1:
            if S=='':
                return 1
            else:
                return 0