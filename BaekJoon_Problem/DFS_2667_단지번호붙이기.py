# BaekJoon 2667번 단지번호붙이기

# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
# 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# 입출력 링크 : https://www.acmicpc.net/problem/2667
# 풀이방법
# (1) 상하좌우 체크함수 만들고고
# (2) 한번 만나면 dfs 로 아파트 다 세버림.
# (3) 세버린 다음 꼭 0으로 초기화
# (4) 다시 전체 맵에 대한 반복문 돌면서 또 아파트 만나면 쭈루루룩
import sys

# dx, dy는 한 점기준으로 상하좌우 체크한 것
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 사각형 크기 구하기
n = int(sys.stdin.readline())
a = [list(sys.stdin.readline().strip()) for _ in range(n)]
cnt = 0
apt =[]

# dfs
def dfs(x, y):
    global cnt
    a[x][y]='0'
    cnt += 1

    # 4방향 검사해서 한방향씩 dfs 만약 해당 곳이 1이면 0으로 바꾸고 cnt ++
    for i in range(4):
        nx = x+dx[i]; ny = y+dy[i]
        # 기준범위 밖일 때
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if a[nx][ny] == '1':
            dfs(nx, ny)

# 전범위중 1인것들만
for i in range(n):
    for j in range(n):
        if a[i][j] == '1':
            cnt = 0
            dfs(i,j)
            apt.append(cnt)

# 단지 정렬
apt.sort()

# 단지 갯수와 단지별 아파트 수 출력
print(len(apt))
for i in apt:
    print(i)