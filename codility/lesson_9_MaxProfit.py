
# O(N) => 100%
def solution(A):
    prev_value = 200000
    profit = 0
    maxProfit = 0
    for i in range(1,len(A)):
        if prev_value > A[i-1]: 
            prev_value = A[i-1]
        # 이전값과의 차이를 구해보고 차이가 양수가 아닌 음수면 버리기 (=> 0으로 초기화 해림)
        profit = max(0, A[i]-prev_value)
        # 가장 max값이였던 때를 남기는 것
        maxProfit = max(profit, maxProfit) 
    return maxProfit


# O(N^2) => 66%
def solution(A):
    max_profit = 0
    for i in range(0, len(A)-1):
        for j in range(i+1, len(A)):
            profit = A[j] - A[i]
            if profit >= max_profit:
                max_profit = profit
    return max_profit