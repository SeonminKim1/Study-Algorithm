# BaekJoon 9012번 괄호

# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
# 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
# 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다.
# 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다.
# 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다.
# 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다.
# 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.
# 입출력 링크 : https://www.acmicpc.net/problem/9012

# [1] 일반 풀이법
# 풀이 아이디어
# (1) '(' 는 ')' 보다 항상 먼저 와야됨 -> '('는 + ')'는 -일때 리스트가 추가되면서 최소한 양수가 와야함
# (2) 음수되는 순간 끝임
# (3) 최종적으로는 음수이거나 양수인 경우는 안되고 0인 경우만 됨.

import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    ps = list(sys.stdin.readline().strip())
    
    # state가 무조건 0이상이여야된다고 가정
    state = 0
    stack = []
    for i in ps:
        stack.append(i)
        if i == '(':
            state+=1
        elif i==')':
            state-=1
        if state<0:
            break
    if state==0:
        print('YES')
    # 0보다 작거나 크거나
    else:
        print('NO')



# [2] 스택 이용 풀이법
# 풀이 아이디어
# (1) list 괄호 한개씩 넣는다.
# (2) '(' 일 경우에는 stack을 쌓고, ')'일 경우에는 stack을 제거한다.
# (3) 단 stack이 비어있는데 ')' 가 온 경우에는 x
import sys
T = int(sys.stdin.readline())

for _ in range(T):
    stack = []
    state = True
    ps = list(sys.stdin.readline().strip())

    for i in ps:
        if i=='(':
            stack.append(i)
        # i == ')' 인 경우
        else :
            # 비어있는 경우
            if len(stack)==0:
                state = False
                break
            else:
                stack.pop()
    # 최종 체크
    if state == True and len(stack)==0:
        print('YES')
    # '('가 더 많을떄, ')' 가 더 많을때
    else:
        print('NO')

