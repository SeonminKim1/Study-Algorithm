# 짝수 => int(n/2), n/2 -1 
# 홀수 => int(n/2), n/2

def solution(s):
    # case 1
    idx = int(len(s)/2)
    if len(s)%2==0:
        return s[idx-1:idx+1]
    else:
        return s[idx]

    # case 2 
    # 짝수 : 4 => 1.5 ~ 3
    # 홀수 : 5 => 2 ~ 3.5
    # return s[(len(s)-1)//2:len(s)//2+1]
