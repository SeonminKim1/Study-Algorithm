# BaekJoon 10828 스택

# 스택 기본인 push / pop / size / empty / top 구현
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 입출력 링크 : https://www.acmicpc.net/problem/10828

import sys

# testcase
N = int(sys.stdin.readline().strip())

stack = []
for _ in range(N):
    order = list(sys.stdin.readline().strip().split())

    # push
    if order[0] == 'push':
        stack.append(int(order[1]))

    # pop
    elif order[0]=='pop':
        if len(stack) == 0:
            print(-1)
        else:
            pop_num = stack.pop()
            print(pop_num)

    # top
    elif order[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            top_num = stack[-1]
            print(top_num)

    # size
    elif order[0] == 'size':
        print(len(stack))

    # empty
    elif order[0] == 'empty':
        if len(stack)==0:
            print(1)
        else :
            print(0)