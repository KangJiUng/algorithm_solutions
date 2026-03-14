# T는 민트를, C는 초코를, M은 우유
# AI 도움

import sys
from collections import deque

input = sys.stdin.readline

# 음식 비트마스크
food_map = {"T": 1, "C": 2, "M": 4}

# 방향 (위 아래 왼쪽 오른쪽)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 전파 순서(비트마스크 or 연산)
spread_order = [1, 2, 4, 6, 5, 3, 7]

# 출력 순서(비트마스크 or 연산)
answer_order = [7, 3, 5, 6, 4, 2, 1]


# BFS
def make_groups(n, food, faith):
    visited = [[False] * n for _ in range(n)]
    groups = []

    for i in range(n):
        for j in range(n):

            if visited[i][j]:
                continue

            q = deque([(i, j)])
            visited[i][j] = True

            members = [(i, j)]
            f = food[i][j]

            while q:
                r, c = q.popleft()

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < n and 0 <= nc < n:
                        if not visited[nr][nc] and food[nr][nc] == f:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                            members.append((nr, nc))

            # 대표자 찾기
            lr, lc = members[0]
            for r, c in members:
                # 신앙심이 더 큰 사람이 대표자
                if faith[r][c] > faith[lr][lc]:
                    lr, lc = r, c

                elif faith[r][c] == faith[lr][lc]:
                    # 신앙심이 동일한 경우 r -> c 순으로 작은 사람이 대표자
                    if r < lr or (r == lr and c < lc):
                        lr, lc = r, c

            groups.append((f, members, lr, lc))

    return groups


def lunch_time(n, food, faith):
    groups = make_groups(n, food, faith)
    leaders = []

    for f, members, lr, lc in groups:
        size = len(members)

        for r, c in members:
            # 대표자면 넘김(그룹원 신앙심 대표자에게 넘기는 중)
            if r == lr and c == lc:
                continue

            faith[r][c] -= 1

        # 대표자 신앙심 추가
        faith[lr][lc] += size - 1
        leaders.append((f, lr, lc, faith[lr][lc]))

    return leaders


def evening_time(n, food, faith, leaders):
    defended = [[False] * n for _ in range(n)]

    single = []
    double = []
    triple = []

    for f, r, c, b in leaders:
        if f in (1, 2, 4):
            single.append((f, r, c, b))
        elif f in (6, 5, 3):
            double.append((f, r, c, b))
        else:
            triple.append((f, r, c, b))

    single.sort(key=lambda x: (-x[3], x[1], x[2]))
    double.sort(key=lambda x: (-x[3], x[1], x[2]))
    triple.sort(key=lambda x: (-x[3], x[1], x[2]))

    for group in (single, double, triple):
        for f, r, c, _ in group:
            # 방어상태면 넘어감
            if defended[r][c]:
                continue

            b = faith[r][c]
            x = b - 1
            faith[r][c] = 1

            if x <= 0:
                continue

            d = b % 4
            nr = r + dr[d]
            nc = c + dc[d]
            my_food = food[r][c]

            while 0 <= nr < n and 0 <= nc < n and x > 0:
                if food[nr][nc] == my_food:
                    nr += dr[d]
                    nc += dc[d]
                    continue

                defended[nr][nc] = True
                y = faith[nr][nc]

                if x > y:
                    food[nr][nc] = my_food
                    x -= y + 1
                    faith[nr][nc] += 1
                else:
                    food[nr][nc] |= my_food
                    faith[nr][nc] += x
                    x = 0
                    break

                nr += dr[d]
                nc += dc[d]


def get_result(n, food, faith):
    result = [0] * 8

    for i in range(n):
        for j in range(n):
            result[food[i][j]] += faith[i][j]

    return [result[k] for k in answer_order]


def solution(n, food, faith):
    # 아침
    for i in range(n):
        for j in range(n):
            faith[i][j] += 1

    # 점심
    leaders = lunch_time(n, food, faith)

    # 저녁
    evening_time(n, food, faith, leaders)

    return get_result(n, food, faith)


if __name__ == "__main__":

    n, t = map(int, input().split())

    food = []

    for _ in range(n):
        row = input().strip()
        food.append([food_map[ch] for ch in row])

    faith = [list(map(int, input().split())) for _ in range(n)]

    for _ in range(t):
        ans = solution(n, food, faith)
        print(*ans)
