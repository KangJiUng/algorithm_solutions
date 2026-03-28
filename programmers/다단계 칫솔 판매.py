def solution(enroll, referral, seller, amount):
    n = len(enroll)

    # 이름 -> 번호
    idx = {}
    for i in range(n):
        idx[enroll[i]] = i

    # 부모(추천인) 배열
    parent = [-1] * n
    for i in range(n):
        if referral[i] != "-":
            parent[i] = idx[referral[i]]

    # 각 사람이 최종적으로 가져가는 돈
    profit = [0] * n

    # 판매 처리
    for i in range(len(seller)):
        cur = idx[seller[i]]
        money = amount[i] * 100  # 칫솔 1개당 100원

        while cur != -1 and money > 0:
            up = money // 10  # 추천인에게 줄 돈
            mine = money - up  # 내가 가질 돈

            profit[cur] += mine
            cur = parent[cur]
            money = up

    return profit
