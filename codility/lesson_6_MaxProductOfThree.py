# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# O(N^3)
def solution(A): 
    max_value = 0
    for i in A:
        for j in A:
            for k in A:
                if max_value <= i*j*k:
                    max_value = i*j*k
    return max_value

def solution(A):
    A.sort()
    return max(A[0]*A[1]*A[-1],A[-3]*A[-2]*A[-1])