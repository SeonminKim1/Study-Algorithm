# BaekJoon 1874번 스택 수열

# 스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다.
# 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가
# 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
# 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면
# 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
# 이를 계산하는 프로그램을 작성하라.

# 입출력 링크 : https://www.acmicpc.net/problem/1874

# [1] 일반 풀이법
# (1) 문제를 이해하는 게 중요. 특정 수열을 입력하는 것
# (2) 4입력시 4까지 생성 -> 3입력시 이미 생성했으므로 x / 6입력 5,6 추가 생성
# (3) 맨뒤 문자가 내 수열과 맞으면 이 수열은 가능한 것
import sys
n = int(sys.stdin.readline())

stack = []
result=[]
num = 1
stop = 1
for _ in range(n):
    m = int(sys.stdin.readline())
    for i in range(stop, m+1):
        stack.append(i)
        result.append('+')
        stop = stop + 1
    if stack[-1]==m:
        stack.pop()
        result.append('-')
    else:
        print('No')
        exit(0)
        break
print('\n'.join(result))

