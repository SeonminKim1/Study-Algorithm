from collections import Counter

def solution(A):
    half = int(len(A)//2) + 1
    most_count_num = [ i for i in Counter(A).most_common(1) if i[1]>=half ] # [(3, 4), (2,2)]
    if len(most_count_num)==0:
        return -1
    return A.index(most_count_num[0][0])