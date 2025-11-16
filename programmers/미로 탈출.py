from collections import deque


def bfs(start, target, maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    q = deque([start])
    visited[start[0]][start[1]] = 1

    # 이동 방향 (상, 하, 좌, 우)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()

        # 목표 지점 도착 시 거리 반환
        if maps[x][y] == target:
            return visited[x][y] - 1  # 시작칸 제외한 이동 횟수

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 맵 범위 내 & 벽(X) 아님 & 미방문
            if (
                0 <= nx < n
                and 0 <= ny < m
                and maps[nx][ny] != "X"
                and not visited[nx][ny]
            ):
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return -1


def solution(maps):
    n, m = len(maps), len(maps[0])
    start = lever = exit = (0, 0)

    # 시작, 레버, 출구 위치 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)
            elif maps[i][j] == "E":
                exit = (i, j)

    # S -> L
    to_lever = bfs(start, "L", maps)
    if to_lever == -1:
        return -1

    # L -> E
    to_exit = bfs(lever, "E", maps)
    if to_exit == -1:
        return -1

    # 총 거리 반환
    return to_lever + to_exit
