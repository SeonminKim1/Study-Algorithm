# The goal is to find the minimal perimeter of any rectangle
def solution(N):
    min_area = float('+inf')
    i = 1
    perimeter = 0
    while i*i <= N:
        if i*i == N:
            perimeter = 2 * (i+i)
        elif N%i == 0:
            perimeter = 2 * (i + N//i)
        i+=1
        if perimeter <= min_area:
            min_area = perimeter
    return min_area