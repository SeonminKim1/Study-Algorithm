# N개의 Counter [0,0,0,...]
# X는 index
# A[K]가 len(N)+1 일 때 max_counter
# A[K]가 X면 increase
# Version 1 => 66%
def solution(N, A):
    count_list = [0]*N
    for i in A:
        if i != N+1:
            count_list[i-1] += 1
        else:
            count_list = [max(count_list)]*N
    return count_list

# =================
# Version 2 => 77%
def solution(N, A):
    count_list = [0]*N 
    max_value = 0
    for i in A:
        if i != N+1:
            count_list[i-1] += 1
            val = count_list[i-1]
            if max_value < val:
                max_value = val
        else:
            count_list = [max_value]*N
    return count_list