# BaekJoon 1931번 회의실배정

# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
# 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고,
# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라.
# 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
# 회의의 시작시간과 끝나는 시간이 같을 수도 있다.
# 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

# 입출력 링크 : https://www.acmicpc.net/problem/1931
# 참고 링크 : https://daimhada.tistory.com/38

# 예상 풀이법
# (1) 시작시간 기준으로 정렬하고, 종료시간 기준으로 한번더 정렬한다.
# (2) 그렇게 하면 (1,4), (1,2) 이런것도 즉 동시간대에 시작하는 것 중 최소시간인 것들이 앞으로온다.
# (3) 회의 종료시간을  시작가능시간으로 바꿔가면서 천천히 채워나감.

import sys

def greedy(meeting):
    meeting_count = 0
    s_time = 0
    for i in meeting:
        if i[0]>=s_time:
            meeting_count+=1
            s_time = i[1]
    return meeting_count


if __name__=="__main__":
    N = int(sys.stdin.readline().strip())
    meeting = []
    for i in range(N):
        s_time, e_time = map(int, sys.stdin.readline().strip().split(' '))
        meeting.append((s_time, e_time))

    # 시작 시간 기준으로 정렬
    meeting = sorted(meeting, key=lambda x:x[0])

    # 종료 시간 기준으로 한번더 정렬
    meeting = sorted(meeting, key=lambda x:x[1])

    result = greedy(meeting)
    print(result)
