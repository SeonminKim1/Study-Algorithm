# BaekJoon 1463 1로 만들기

# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
 
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.

# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 입출력 링크 : https://www.acmicpc.net/problem/1463

# 풀이방법
# (1) 계산을 진행한 list를 계속 그 함수로 넘겨주는 것
# (2) 그 후 count ++
# (3) 배열중에 1이 있을 경우 break
# ex 10일 경우
# 1: [9,5]
# 2: [8,3,4]
# 3: [7,4,2,1,3,2]

x = int(input())
start = [x]

def dp(array):
    ls = []
    for i in array:
        ls.append(i-1)
        if i%3==0:
            ls.append(i/3)
        if i%2==0:
            ls.append(i/2)
    return ls

count =0
while True:
    if x==1:
        break
    temp = start[:]
    start = []
    start = dp(temp)
    #print(count+1, ':', start)
    count+=1
    if (min(start))==1:
        break

print(count)

