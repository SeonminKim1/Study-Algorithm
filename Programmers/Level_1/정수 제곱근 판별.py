def solution(n):
    root_num = n ** (1/2)
    if root_num%1 == 0:
        return (root_num+1) **2
    else:
        return -1