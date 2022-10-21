def solution(sizes):
    # w, h 
    # 두 w, h 중에 w가 큰 값, h가 작은 값들이 오게 몰음
    # max(w_list), max(h_list) 곱하면됨
    w_list, h_list =[], []
    for w, h in sizes:
        if w<h:
            w, h = h, w
        w_list.append(w)
        h_list.append(h)
    return max(w_list) * max(h_list)
