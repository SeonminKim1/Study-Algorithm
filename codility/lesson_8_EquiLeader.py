# two sequences 
# - A[0], A[1], ..., A[S] 
# - A[S + 1], A[S + 2], ..., A[N - 1] have leaders of the same value

def solution(A):
    leader1_dict, leader2_dict = {}, {}
    leader1_len, leader2_len = len(A), 0
    cnt = 0
    # 1. 총 갯수 초기화 - leader1_dict
    for n in A:
        if n not in leader1_dict:
            leader1_dict[n] = 1
        else:
            leader1_dict[n] += 1

    # 2. 1개씩 빼면서 leader2_dict에 옮기기
    leader2_num, leader2_count = 0, 0
    for n in A:
        leader1_dict[n] -= 1
        leader1_len -= 1
        if n not in leader2_dict:
            leader2_dict[n] = 1
        else:
            leader2_dict[n] += 1
        leader2_len += 1   
        # print(leader1_dict, leader2_dict)
        # 3. 한번 옮길 때마다 leader2의 cnt가 가장 높은 값인지 확인
        if leader2_dict[n] > leader2_count:
            leader2_count = leader2_dict[n]
            leader2_num = n
        
        # 2에서 구하고 Leader num을 1과 같은지 확인 (=1에서 Leader인지, half 넘는지)
        if  (leader2_count > leader2_len/2) and \
            (leader1_dict[leader2_num] > leader1_len/2):
            # print(leader2_len, leader1_len, leader2_num, leader2_count)
            cnt+=1
    return cnt





# =========== O(N^2) => Performance x
from collections import Counter
def solution(A):
    cnt=0
    for idx in range(0, len(A)-1): # len(A)-1=5, idx 0~4
        l1, l2 = A[:idx+1], A[idx+1:]
        cnt_num1 = Counter(l1).most_common(1) # [(4:2)]
        cnt_num2 = Counter(l2).most_common(1) # [(4:2)]

        l1_half, l2_half = int(len(l1)//2)+1, int(len(l2)//2)+1

        if cnt_num1[0][1] >= l1_half and \
            cnt_num2[0][1] >= l2_half and \
            cnt_num1[0][0] == cnt_num2[0][0]:
                cnt+=1
    return cnt