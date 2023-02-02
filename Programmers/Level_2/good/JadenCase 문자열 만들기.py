# 공백이 사이에 여러번 나올수 있어서
# 이전단어가 공백이고, 이후단어가 word 인지 확인이 핵심
def solution(s):
    answer = s[0].upper() 
    for i in range(1, len(s)):
        if s[i-1] == " " and s[i] != " ":
            answer += s[i].upper() 
        else:
            answer += s[i].lower()
    return answer
