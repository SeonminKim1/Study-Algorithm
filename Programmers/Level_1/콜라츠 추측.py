def solution(num):
    count = 0
    if num == 1:
        return 0
    for _ in range(1, 501):
        if num%2==0:
            num=num/2
        else:
            num=num*3+1        
        count+=1                
        if num==1:
            return count
    return -1