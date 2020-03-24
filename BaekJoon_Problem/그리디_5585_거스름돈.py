# BaekJoon 5585번 거스름돈

# 타로는 자주 JOI잡화점에서 물건을 산다.
# JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고,
# 언제나 거스름돈 개수가 가장 적게 잔돈을 준다.
# 타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때,
# 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.

# 입출력 링크 : https://www.acmicpc.net/problem/5585

# 예상 풀이법

import sys

money = int(sys.stdin.readline().strip())
coins = [500, 100, 50, 10, 5, 1]
remains = 1000-money
count = 0
for i in range(len(coins)):
    # 금액을 다채웠으면 break
    if remains == 0:
        break
    # 접근금액단위가 원하는 금액보다 클 때
    if coins[i] > remains:
        continue
    # 몫(동전)의 갯수를 더함
    count += remains // coins[i]
    # 나머지 최신화
    remains %= coins[i]

print(count)