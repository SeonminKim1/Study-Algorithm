# BaekJoon 1541번 잃어버린 괄호

# 세준이는 양수와 +, -, 그리고 괄호를 가지고 길이가 최대 50인 식을 만들었다.
# 그리고 나서 세준이는 괄호를 모두 지웠다.
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고,
# 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고,
# 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다.

# 입출력 링크 : https://www.acmicpc.net/problem/2875

# 풀이방법
# (1) - 이후에 괄호를 치면된다.
# (2) - 와  + 가 반복해서 나오므로 첫 숫자에서 모든 숫자를 다 빼면됨.

minus = input().split('-')
result =[]
# print('minus',minus)
for i in minus:
    sum = 0
    plus = i.split('+')
    # print('plus',plus)
    for j in plus:
        sum +=int(j)
    # 각 괄호안에 있는 +들 숫자 다 더한게 sum
    result.append(sum)

# 맨 처음값 result[0]
sum_min = result[0]
for i in range(1, len(result)):
    sum_min-=result[i]

print(sum_min)