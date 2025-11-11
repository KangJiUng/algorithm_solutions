# 0은 벽이 있는 자리, 1은 벽이 없는 자리
# 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에
# 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에


from collections import deque


def solution(maps):
    # 테두리 추가 (모두 0)
    maps.insert(0, [0 for i in range(len(maps[0]))])
    maps.append([0 for j in range(len(maps[0]))])
    for row in maps:
        row.insert(0, 0)
        row.append(0)

    # 테두리 추가 후 크기 재정의
    n = len(maps)
    m = len(maps[0])

    # visited 크기 맞춰서 생성
    visited = [[0 for j in range(m)] for i in range(n)]

    # 이동 방향 (동, 서, 남, 북)
    dir_x = [1, -1, 0, 0]
    dir_y = [0, 0, 1, -1]

    # BFS 초기화
    q = deque()
    q.append((1, 1))
    visited[1][1] = 1  # 시작 지점까지 거리(칸 개수 + 1)

    while q:
        x, y = q.popleft()

        # 도착 지점 확인 (원래의 우하단 좌표 → 테두리 기준으로 맞추기)
        if x == n - 2 and y == m - 2:
            return visited[x][y]

        # 4방향 탐색
        for i in range(4):
            next_x = x + dir_x[i]
            next_y = y + dir_y[i]
            if maps[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                visited[next_x][next_y] = visited[x][y] + 1
                q.append((next_x, next_y))

    # 도달 불가능 시
    return -1
