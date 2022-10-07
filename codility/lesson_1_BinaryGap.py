def solution(N):
    number = bin(N)[2:]
    one_list = []
    for idx, s in enumerate(number):
        if s == '1':
            one_list.append(idx)
    
    # [0, 4, 7]
    if len(one_list)<2:
        return 0
    else:
        max_num = 0
        for i in range(len(one_list)-1):
            gap = one_list[i+1] - one_list[i]-1
            if gap > max_num:
                max_num = gap
        return max_num