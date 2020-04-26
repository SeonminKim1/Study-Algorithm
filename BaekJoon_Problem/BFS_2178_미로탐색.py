# BaekJoon 2178번 미로탐색

# N×M크기의 배열로 표현되는 미로가 있다.
#   1	0	1	1	1	1
#   1	0	1	0	1	0
#   1	0	1	0	1	1
#   1	1	1	0	1	1

# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때
# 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
#
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
# 입출력 링크 : https://www.acmicpc.net/problem/2178

import sys
N, M = map(int, sys.stdin.readline().strip().split(' '))

map_list = [list(sys.stdin.readline().strip()) for _ in range(N)]

visit = [[0]*M for _ in range(N)]
need_visit=[]
dx = [-1, 0 ,1 ,0 ] # 왼쪽, 위, 오른쪽, 아래
dy = [0, -1, 0, 1 ]

need_visit = []
need_visit.append((0,0))
visit[0][0] = 1

while need_visit:
    b, a = need_visit.pop(0)
    # 미로의 끝에 도달하면 끝
    if b == N-1 and a == M-1:
        print(visit[b][a])
        sys.exit()
    # 4방향 체크
    for i in range(4):
        b2, a2 = b + dy[i], a + dx[i] # (0, -1) , (-1, 0), (0, 1) , (1,0)

        # 범위 안이고 and 방문한 기록이 없으며 미로상 길인경우
        if b2>=0 and b2<N and a2>=0 and a2<M:
            if visit[b2][a2]==0 and map_list[b2][a2]=='1':
                visit[b2][a2] = visit[b][a] + 1
                need_visit.append((b2, a2))
