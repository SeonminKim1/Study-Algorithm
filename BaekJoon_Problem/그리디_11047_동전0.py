# BaekJoon 11047번 동전0

# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

# 입출력 링크 : https://www.acmicpc.net/problem/11047

# 예상 풀이법
# (1) 가장높은 금액부터 차례대로 나눔
# (2) 잔액이 0이면 끝 / 비교금액이 원하는 금액보다 클 경우 continue
# (3) 곱 ( // ) 과 나머지 ( % ) 로 해결

import sys
N, K = map(int, sys.stdin.readline().strip().split())

value_list = []
count = 0 # 몫의 갯수
for _ in range(N):
    v = int(sys.stdin.readline().strip())
    value_list.append(v)

for i in range(N - 1, -1, -1):
    # 금액을 다채웠으면 break
    if K == 0:
        break
    # 접근금액단위가 원하는 금액보다 클 때
    if value_list[i] > K:
        continue

    # 몫(동전)의 갯수를 더함
    count += K // value_list[i]
    # 나머지 최신화
    K %= value_list[i]

print(count)