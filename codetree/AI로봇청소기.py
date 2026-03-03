# 검색, AI 도움

from collections import deque


def main():
    n, k, l = map(int, input().split())

    # 격자 정보 입력 받기
    board = [list(map(int, input().split())) for _ in range(n)]

    robots = []
    robot_grid = [[False] * n for _ in range(n)]

    # 로봇 위치 입력 받기
    for _ in range(k):
        r, c = map(int, input().split())
        robots.append([r - 1, c - 1])
        robot_grid[r - 1][c - 1] = True

    # 4방향 청소 방향
    clean_shapes = [
        [(0, 0), (-1, 0), (1, 0), (0, 1)],  # 오른쪽 방향
        [(0, 0), (0, -1), (0, 1), (1, 0)],  # 아래쪽 방향
        [(0, 0), (-1, 0), (1, 0), (0, -1)],  # 왼쪽 방향
        [(0, 0), (0, -1), (0, 1), (-1, 0)],  # 위쪽 방향
    ]

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def is_valid_position(r, c):
        return 0 <= r < n and 0 <= c < n

    def move_robots():
        """로봇 이동: BFS로 가장 가까운 먼지 찾기"""
        for i in range(k):
            curr_r, curr_c = robots[i]

            # 이미 현재 위치에 먼지가 있다면 이동하지 않음
            if board[curr_r][curr_c] > 0:
                continue

            # 이동을 위해 내 위치를 일단 비움 (다른 로봇과 겹치지 않게)
            robot_grid[curr_r][curr_c] = False

            q = deque([(curr_r, curr_c, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[curr_r][curr_c] = True

            found_dist = -1
            candidates = []

            while q:
                r, c, dist = q.popleft()

                # 이미 찾은 최단 거리보다 멀어지면 탐색 종료
                if found_dist != -1 and dist > found_dist:
                    break

                # 먼지를 찾은 경우
                if board[r][c] > 0:
                    if found_dist == -1:
                        found_dist = dist
                    candidates.append((r, c))
                    continue  # 목적지를 찾았으므로 이 경로로는 더 깊이 안 감

                # 상하좌우 탐색
                for d_idx in range(4):
                    nr, nc = r + dr[d_idx], c + dc[d_idx]
                    if is_valid_position(nr, nc):
                        # 방문 안 했고, 물건(-1) 없고, 다른 로봇(True) 없는 곳만 이동
                        if (
                            not visited[nr][nc]
                            and board[nr][nc] != -1
                            and not robot_grid[nr][nc]
                        ):
                            visited[nr][nc] = True
                            q.append((nr, nc, dist + 1))

            if candidates:
                # 행 우선, 열 우선 정렬
                candidates.sort()
                next_r, next_c = candidates[0]
                robots[i] = [next_r, next_c]
                robot_grid[next_r][next_c] = True  # 새 위치 등록
            else:
                # 못 찾았으면 제자리 유지
                robot_grid[curr_r][curr_c] = True

    def clean_dust():
        """로봇 청소"""
        for i in range(k):
            r, c = robots[i]
            max_clean = -1
            best_shape_idx = -1

            # 합이 같은 방향이 여러개인 경우, 오른쪽, 아래쪽, 왼쪽, 위쪽 방향의 우선순위로 방향을 선택하므로
            # 4가지 모양을 대조 (0: 우, 1: 하, 2: 좌, 3: 상)
            for s_idx, shape in enumerate(clean_shapes):
                current_clean = 0
                for d_r, d_c in shape:
                    nr, nc = r + d_r, c + d_c
                    if is_valid_position(nr, nc) and board[nr][nc] > 0:
                        current_clean += min(board[nr][nc], 20)

                # > 를 사용하면 양이 같을 때 먼저 계산된 우, 하 방향이 우선권을 유지함
                if current_clean > max_clean:
                    max_clean = current_clean
                    best_shape_idx = s_idx

            # 가장 먼지를 많이 치우는 모양으로 격자 업데이트
            if best_shape_idx != -1:
                for d_r, d_c in clean_shapes[best_shape_idx]:
                    nr, nc = r + d_r, c + d_c
                    if is_valid_position(nr, nc) and board[nr][nc] > 0:
                        board[nr][nc] = max(0, board[nr][nc] - 20)

    def accumulate_dust():
        """먼지 축적"""
        for r in range(n):
            for c in range(n):
                if board[r][c] > 0:
                    board[r][c] += 5

    def spread_dust():
        """먼지 확산"""
        # 동시 확산을 위해 더해질 값을 따로 저장할 배열
        diff_add = [[0] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if board[r][c] == 0:  # 깨끗한 격자에만 확산
                    adj_sum = 0

                    for d_idx in range(4):
                        nr, nc = r + dr[d_idx], c + dc[d_idx]
                        if is_valid_position(nr, nc) and board[nr][nc] > 0:
                            adj_sum += board[nr][nc]

                    diff_add[r][c] = adj_sum // 10

        # 격자에 확산된 먼지량 일괄 적용
        for r in range(n):
            for c in range(n):
                board[r][c] += diff_add[r][c]

    # 테스트 L번 실행
    for _ in range(l):
        move_robots()
        clean_dust()
        accumulate_dust()
        spread_dust()

        # 각 턴 종료 시 총 먼지량 합산 및 출력
        total_dust = 0
        for r in range(n):
            for c in range(n):
                if board[r][c] > 0:
                    total_dust += board[r][c]
        print(total_dust)


main()
