# 풀이 1 - 런타임 에러
def solution(n, m, x, y, r, c, k):
    # 이동 방향: 사전순 (d, l, r, u)
    dirs = [("d", 1, 0), ("l", 0, -1), ("r", 0, 1), ("u", -1, 0)]

    def dfs(cur_x, cur_y, path, remain):
        # 현재 위치에서 도착점까지 최소 거리(절댓값 이용)
        # x 이동 횟수 + y 이동 횟수
        dist = abs(cur_x - r) + abs(cur_y - c)

        # 도착 불가능
        # 앞으로 쓸 수 있는 이동 횟수가 최소 거리보다 작거나
        # (이동 횟수 - 최소 거리) 가 홀수거나(왔다갔다로 안됨)
        if dist > remain or (remain - dist) % 2 != 0:
            return None

        # k번 이동
        if remain == 0:
            # 이동완
            if cur_x == r and cur_y == c:
                return path

            return None

        # 사전순 DFS
        for d, dx, dy in dirs:
            new_x, new_y = cur_x + dx, cur_y + dy

            # 격자 바깥 아니면
            if 1 <= new_x <= n and 1 <= new_y <= m:
                # 이동횟수 줄이며 새로운 방향으로
                result = dfs(new_x, new_y, path + d, remain - 1)

                if result is not None:
                    return result

        return None

    answer = dfs(x, y, "", k)

    if answer is not None:
        return answer
    else:
        return "impossible"


# 풀이 2 - 그리디
def solution(n, m, x, y, r, c, k):
    # 이동 방향: 사전순 (d, l, r, u)
    dirs = [("d", 1, 0), ("l", 0, -1), ("r", 0, 1), ("u", -1, 0)]

    cur_x, cur_y = x, y
    remain = k
    path = []

    while remain > 0:
        moved = False

        for d, dx, dy in dirs:
            new_x, new_y = cur_x + dx, cur_y + dy

            # 격자 바깥이면 스킵
            if not (1 <= new_x <= n and 1 <= new_y <= m):
                continue

            dist = abs(new_x - r) + abs(new_y - c)
            if dist > remain - 1 or (remain - 1 - dist) % 2 != 0:
                continue

            # 이 방향은 끝까지 가능
            path.append(d)
            cur_x, cur_y = new_x, new_y
            remain -= 1
            moved = True
            break

        # 어떤 방향도 못 가면 불가능
        if not moved:
            return "impossible"

    return "".join(path)
