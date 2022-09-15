'''
유클리드 호제법 (gcd, lcm 구하기)
1. a와 b (a<b) r=a%b
2. r==0이 될 때까지 r=b%r 
3. 했을 때 r이 최대공약수
4. 최소공배수는 (a*b)/최대공약수

## case 1
a, b, r
2, 5, 2 # r=a%b
2, 5, 1 # r=b%r
2, 5, 0 # 직전 r 최대공약수

## case 2
a, b,  r
8, 12, 8 # r=a%b
8, 12, 4 # r=b%r
8, 12, 0 # 직전 r 최대공약수
'''
def solution(n, m):
    c, d = max(n, m), min(n, m)
    gcd = 1
    while gcd > 0:
        gcd = c % d
        c, d = d, gcd
    answer = [c, int(n*m/c)]
    return answer
