# 경주로를 건설하는 데 필요한 최소 비용

import heapq


# AI 도움
def solution(board):
    answer = 0
    N = len(board)

    # 최대 이동 칸 수(25 * 25) * 한 이동당 최대 비용(600)
    MAX_COST = 375000

    # 0: 위, 1: 오른쪽, 2: 아래, 3: 왼쪽
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # cost[x][y][d]
    # d 방향으로 들어와서 (x, y)에 도착해 있는 상태의 최소 비용
    # d는 이 칸에 오기 직전에 이동했던 방향
    cost = [[[MAX_COST] * 4 for _ in range(N)] for _ in range(N)]

    # 우선순위 큐: (누적 비용, x, y, 이전 방향 d)
    pq = []

    # 아래 두 상태로 시작한다고 보면 된다.
    # (0, 0)에 오른쪽 방향(1)으로 들어와 있는 상태
    # (0, 0)에 아래 방향(2)으로 들어와 있는 상태
    for d in (1, 2):
        cost[0][0][d] = 0
        heapq.heappush(pq, (0, 0, 0, d))

    while pq:
        # 튜플 언패킹
        cur_cost, x, y, d = heapq.heappop(pq)

        # 이미 더 싼 비용으로 같은 상태에 도달한 적이 있으면 스킵
        if cur_cost > cost[x][y][d]:
            continue

        # 다음에 이동할 방향 nd를 모두 시도
        for nd in range(4):
            nx = x + dx[nd]
            ny = y + dy[nd]

            # 범위 밖이면 불가
            if not (0 <= nx < N and 0 <= ny < N):
                continue

            # 벽이면 불가
            if board[nx][ny] == 1:
                continue

            # 기본 이동 비용: 직선 포함 100
            new_cost = cur_cost + 100

            # 이전 방향(d)과 다음 방향(nd)이 다르면 코너
            # 추가 비용 500
            if nd != d:
                new_cost += 500

            # (nx, ny)에 nd 방향으로 들어오는 상태의 비용 갱신
            if new_cost < cost[nx][ny][nd]:
                cost[nx][ny][nd] = new_cost
                heapq.heappush(pq, (new_cost, nx, ny, nd))

    # 도착점 (N - 1, N - 1)에 어떤 방향으로 도착했든 그중 최소 비용이 정답
    answer = min(cost[N - 1][N - 1])
    return answer
