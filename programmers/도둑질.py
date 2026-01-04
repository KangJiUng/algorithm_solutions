def get_max(money):
    n = len(money)

    dp = [0] * n
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])

    return dp[-1]


def solution(money):
    n = len(money)

    if n == 0:
        return 0
    if n == 1:
        return money[0]

    # 경우 1: 첫 집 털고, 마지막 집 제외
    case1 = get_max(money[:-1])

    # 경우 2: 첫 집 안 털고, 마지막 집 포함
    case2 = get_max(money[1:])

    return max(case1, case2)
