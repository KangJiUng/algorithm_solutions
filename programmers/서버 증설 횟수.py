def solution(players, m, k):
    answer = 0

    # 서버 증설 때마다 기록(서버 1대가 5시간이라고 하면 1 1 1 1 1 아니고 1 0 0 0 0)
    server_count = [0] * 24

    running = 0

    for i, user in enumerate(players):
        required = user // m

        # k시간 지나면 서버 사라짐
        if i - k >= 0:
            running -= server_count[i - k]

        # 부족하면 증설
        if running < required:
            add = required - running
            server_count[i] = add
            running += add
            answer += add

    return answer
