# BaekJoon 1149 RGB거리

# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i-1번 집의 색과 같지 않아야 한다.

# 입출력 링크 : https://www.acmicpc.net/problem/1149

# 풀이방법
#      R   G   B
# 집1  1   5  10
# 집2  1  10   7
# 집3  7   9  10
#
N = int(input())
cost = []
for i in range(N):
    cost.append(list(map(int, input().split(' '))))

# 빨파초 3번 반복
# 0부터 N-1까지 한다고 하면 바로 반영을 못함 다음것이 그 다음에서는 전에것이 되서 참조가 되버림
# 다음것에서 앞에 것을 끌어다 써야 이어나가기가 좋음
for i in range(1, N):
    # 빨강일때
    red = cost[i][0] + min(cost[i-1][1], cost[i-1][2])
    # 초록일떄
    green = cost[i][1] + min(cost[i-1][0], cost[i-1][2])
    # 파랑일때
    blue = cost[i][2] + min(cost[i-1][0], cost[i-1][1])

    # 방금칠한 집의
    #print(i, ':', red, green, blue)
    cost[i][0], cost[i][1], cost[i][2] = red, green, blue
    #print(cost)
print(min(cost[N-1][0], cost[N-1][1], cost[N-1][2]))
