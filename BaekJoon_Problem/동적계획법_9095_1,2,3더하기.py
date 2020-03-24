# BaekJoon 9095 1,2,3 더하기
# 동적계획법이란
# 특정 범위까지의 값을 구하기 위해서 그것과 다른 범위까지의 값을 이용하여
# 효울적으로 값을 구하는 알고리즘 설계 기법
# 즉 무언의 규칙이 있고 점화식을 세운뒤에 알고리즘을 짜야함?

# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다.
# 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

# 입출력 링크 : https://www.acmicpc.net/problem/9095

# 1 => 1 / 2 => 2 / 3 => 4 /
# 4 => 7 / 5 => 13 / 6 => 24
# f(n) = f(n-3) + f(n-2) + f(n-1)

Test_case = int(input())

for _ in range(Test_case):
    ingredient = [0, 1, 2, 4]
    n = int(input())
    if n<=3:
        hap=ingredient[n]
    else:
        for i in range(4, n+1):
            hap = sum(ingredient[-3:]) # -3부터 뒤에 끝까지
            #print(ingredient[-3:])
            ingredient.append(hap)
    print(hap)
