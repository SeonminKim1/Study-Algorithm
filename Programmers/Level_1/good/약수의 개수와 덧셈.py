def solution(left, right):
    # case 1
    '''
    all_sum = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1): # 1~13
            if i%j==0:
                cnt +=1
        if cnt%2==0:
            all_sum+=i
        else:
            all_sum-=i
    return all_sum
    '''
    
    # case 2
    # 제곱수가 아닌 수의 약수들은 각자 곱해지는 쌍이 있으니까 무조건 약수의 개수가 짝수
    all_sum = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            all_sum -= i
        else:
            all_sum += i
    return all_sum
