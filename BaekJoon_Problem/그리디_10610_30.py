# BaekJoon 10610번 30

# 어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 미르코는 30이란 수를 존경하기 때문에,
# 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.
# 미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.

# 입출력 링크 : https://www.acmicpc.net/problem/10610

# 예상 풀이법
# (1) 30의 배수가 되려면 0이 있어야 하고
# (2) 30의 배수가 되려면 0을 제외한 모든 숫자의 합이 3의 배수여야 함.
# (3) 그중 최댓값이니 내림차순으로 정렬도 필요

N = input()

sum = 0
# 0이 없으면 -1 출력
if '0' not in N:
    print(-1)
    exit(0)

# 각 자리 숫자의 합이 3의 배수일 경우
else:
    for i in N:
        sum += int(i)

    if sum%3==0:
        N = sorted(N, reverse=True)
        print(''.join(N))

    # 합이 3의 배수가 아닐때
    else:
        print(-1)

