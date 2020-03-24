# BaekJoon 1003 피보나치함수
# int fibonacci(int n) {
#     if (n==0) {
#         printf("0");
#         return 0;
#     } else if (n==1) {
#         printf("1");
#         return 1;
#     } else {
#         return fibonacci(n‐1) + fibonacci(n‐2);
#     }
# }
#
# fibonacci(3) 을 호출하면 다음과 같은 일이 일어난다.
# fibonacci(3) 은 fibonacci(2) 와 fibonacci(1) (첫 번째 호출)을 호출한다.
# fibonacci(2) 는 fibonacci(1) (두 번째 호출)과 fibonacci(0) 을 호출한다.
# 두 번째 호출한 fibonacci(1) 은 1을 출력하고 1을 리턴한다.
# fibonacci(0) 은 0을 출력하고, 0을 리턴한다.
# fibonacci(2) 는 fibonacci(1) 과 fibonacci(0) 의 결과를 얻고, 1을 리턴한다.
# 첫 번째 호출한 fibonacci(1) 은 1을 출력하고, 1을 리턴한다.
# fibonacci(3) 은 fibonacci(2) 와 fibonacci(1) 의 결과를 얻고, 2를 리턴한다.
# 이 때, 1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N) 을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

# 풀이방법
# 즉 fibonacci(N)을 호출했을 때 fibonacci(1)과 fibonacci(0)이 몇번호출되었는지 구해야함.
# N값        0 1 2 3 4 5 6 7 8
# 0 호출횟수  1 0 1 1 2 3 5 8 13
# 1 호출횟수  0 1 1 2 3 5 8 13 21
# 호출횟수 또한 피보나치 수열을 따름

# 입출력 링크 : https://www.acmicpc.net/problem/1003

def dp(n):
    if n>=3:
        for i in range(3, n + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
#    print(zero, one)
    print(zero[n], one[n])

T = int(input())
for i in range(T):
    zero = [1, 0, 1]
    one = [0, 1, 1]
    num = int(input())
    dp(num)
