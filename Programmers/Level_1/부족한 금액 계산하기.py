def solution(price, money, count):
    # price => 이용료 price
    # count : 이용 횟수
    # money : 가진돈
    
    # all_price : 놀이기구 총 이용 비용
    all_price = 0
    for i in range(1, count+1):
        # 한번 탑승시 금액 : price*i
        all_price += price * i
    
    # 모자란 금액 : all_price - money
    return 0 if all_price-money <= 0 else all_price-money 