def solution(n):
    answer = [i for i in range(1, n+1) if n%i==0]
    # => range(1, int(n//2)+1) 도 가능. 수의 절반일 때 이미 자기 자신 약수 밖에 남지 않으므로
    return sum(answer)