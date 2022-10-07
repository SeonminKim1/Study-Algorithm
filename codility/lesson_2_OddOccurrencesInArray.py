from collections import Counter

def solution(A):
    for k, v in Counter(A).items():
        if v%2==1:
            return k