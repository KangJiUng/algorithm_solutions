# 모든 구름이 d 방향으로 s칸 이동

n, m = map(int, input().split())
clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]  # 인덱스 반영
board = [list(map(int, input().split())) for _ in range(n)]

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(m):
    d, s = map(int, input().split())

    # 구름 이동
    new_clouds = []
    for r, c in clouds:
        # %n으로 격자 밖으로 나가지 않도록 처리
        nr = (r + dx[d] * s) % n
        nc = (c + dy[d] * s) % n
        new_clouds.append((nr, nc))
        board[nr][nc] += 1  # 비 내리기

    clouds = new_clouds

    # 물복사 버그
    diag = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for r, c in clouds:
        cnt = 0
        for dr, dc in diag:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if board[nr][nc] > 0:
                    cnt += 1

        board[r][c] += cnt

    # 구름 제거
    # 구름이 생기는 칸은 구름이 사라진 칸이 아니어야 한다. (구름 있던 칸은 다시 못 생김)
    cloud_set = set(clouds)

    # 새 구름 생성
    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    new_clouds = []
    for i in range(n):
        for j in range(n):
            if (i, j) not in cloud_set and board[i][j] >= 2:
                new_clouds.append((i, j))
                board[i][j] -= 2

    clouds = new_clouds  # 구름 갱신

# 최종 물의 양 계산
result = 0
for i in range(n):
    for j in range(n):
        result += board[i][j]

print(result)
