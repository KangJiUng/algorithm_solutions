def solution(n, money):
    answer = 0
    MOD = 1000000007

    dp = [0] * (n + 1)
    dp[0] = 1  # 0원을 만드는 방법은 아무 동전도 안 쓰는 1가지

    for coin in money:
        for price in range(coin, n + 1):
            dp[price] += dp[price - coin]
            dp[price] %= MOD

    answer = dp[n]
    return answer
