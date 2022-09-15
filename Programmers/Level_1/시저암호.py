def solution(s, n):
    # case 1
    upper_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lower_list = list('abcdefghijklmnopqrstuvwxyz')
    alphabet_length = 26

    # 각 단어를 n칸씩 밀기
    result = ''
    for word in s:
        if word in upper_list:
            result += upper_list[(upper_list.index(word) + n) % alphabet_length]
        elif word in lower_list:
            result += lower_list[(lower_list.index(word) + n) % alphabet_length]
        else:
            result += word
            pass
    return result

    # case 2
    '''
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
    '''