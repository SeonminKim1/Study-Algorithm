# x=10, y=9 d=10
# x=10, y=70 d=60
def solution(X, Y, D):
    if X>=Y:
        return 0
    elif (Y-X)%D ==0:
        return (Y-X)//D
    else:
        return ((Y-X)//D)+1
