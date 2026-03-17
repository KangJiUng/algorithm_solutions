def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []  # 가격이 아직 안 떨어진 인덱스 저장

    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)

    while stack:
        idx = stack.pop()
        answer[idx] = n - 1 - idx

    return answer
