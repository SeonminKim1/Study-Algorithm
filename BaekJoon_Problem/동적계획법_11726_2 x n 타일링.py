# BaekJoon 11726 2 x n 타일링

# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를
# 구하는 프로그램을 작성하시오.
#
# 아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.
# 입출력 링크 : https://www.acmicpc.net/problem/11726

# n 의 값이
# 1 => 1 / 2=>2 / 3=>3 / 4=> 5 / 5=>8


n = int(input())

# 점화식 f(n) = f(n-2) + f(n-1)
ingredient = [0, 1, 2]
for i in range(3, n+1):
    ingredient.append(sum(ingredient[-2:]))

print(ingredient[n]%10007)