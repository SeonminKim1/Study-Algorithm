# BaekJoon 5397번 스택 수열

# 창영이는 강산이의 비밀번호를 훔치기 위해서 강산이가 사용하는 컴퓨터에 키로거를 설치했다.
# 며칠을 기다린 끝에 창영이는 강산이가 비밀번호 창에 입력하는 글자를 얻어냈다.
# 키로거는 사용자가 키보드를 누른 명령을 모두 기록한다. 따라서, 강산이가 비밀번호를 입력할 때,
# 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낼 수 있다.
# 강산이가 비밀번호 창에서 입력한 키가 주어졌을 때, 강산이의 비밀번호를 알아내는 프로그램을 작성하시오.

# 입출력 링크 : https://www.acmicpc.net/problem/5397

# [1] 예상 풀이 방법
# (1) insert랑 delete만 있으면 append와 pop만 사용해도됨.
# (2) 이문제는 < > 커서 이동도 있기 때문에 스택을 2개를 놓고 왔다갔다를 해야함.
# (3) 기본적으로 입력된건 lstack에서 커서 왼쪽으로(<) 입력시에는 rstack으로
# (4) 반대로 커서 오른쪽으로(>) 입력시에는 rstack에서 lstack으로
# (5) 마지막에는 2개를 합치되 rstack은 reversed된걸로 합쳐야 함.

import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    L = list(sys.stdin.readline().strip())
    print(L)
    lstack = []
    rstack = []
    for i in L:
        # Delete
        if i == '-':
            if lstack:
                lstack.pop()
        # Move Cursor Left
        elif i=='<':
            if lstack:
                a = lstack.pop()
                rstack.append(a)
        # Move Cursor Right
        elif i=='>':
            if rstack:
                a = rstack.pop()
                lstack.append(a)
        # add
        else:
            lstack.append(i)
    lstack.extend(reversed(rstack))
    print(''.join(lstack))