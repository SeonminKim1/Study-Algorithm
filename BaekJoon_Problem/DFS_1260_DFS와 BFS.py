# BaekJoon 1260번 DFS와 BFS

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
# 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 입출력 링크 : https://www.acmicpc.net/problem/2875

# 문제풀이 dfs
# (1) 배열에 색칠.
# (2) 방문했따는 표시 배열 체크 / 해당 행과 열 체크
# (3) 항목이 있으면 거기 들어감 dfs

# 문제풀이 bfs
# (1) 배열에 색칠
# (2) 큐의 맨 첫번째가 현재 출력됬고 그 새 끼들 점검중
# (3) 방문했다는 표시 배열 체크 및 큐에 추가
def dfs(v): # v는 시작점
    # v방문완료
    print(v, end=' ')
    visit[v]=1

    # 해당 행 항목들 체크 v:해당행, i: 차례대로 열들
    for i in range(1, N+1):
        if visit[i] == 0 and s[v][i] ==1:
            dfs(i)

def bfs(v):
    queue=[v]; visit2[v]=1
    while(queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, N+1):
            if visit2[i]==0 and s[v][i]==1:
                queue.append(i)
                visit2[i]=1

N, M, V = map(int, input().split(' '))

s = [[0] * (N+1) for i in range(N+1)]
# [[ 0 0 0 0 ],
# [ 0 0 0 0 ],
# [ 0 0 0 0 ],
# [ 0 0 0 0 ]]
visit = [0 for i in range(N+1)]
visit2 = [0 for i in range(N+1)]
for i in range(M):
    x,y = map(int, input().split(' '))
    s[x][y]=1; s[y][x]=1

dfs(V)
print()
bfs(V)