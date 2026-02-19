# 집을 크기가 R×C인 격자판
# T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양
# AI 도움

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 공기청정기 위치 찾기
cleaner = []
for i in range(r):
    if board[i][0] == -1:
        cleaner.append(i)

upper = cleaner[0]
lower = cleaner[1]


# 1. 미세먼지 확산
def spread():
    new_board = [[0] * c for _ in range(r)]

    # 공기청정기 위치 반영
    new_board[cleaner[0]][0] = -1
    new_board[cleaner[1]][0] = -1

    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                amount = board[i][j] // 5
                spread_count = 0

                for d in range(4):
                    ni = i + dy[d]
                    nj = j + dx[d]

                    if 0 <= ni < r and 0 <= nj < c and board[ni][nj] != -1:
                        new_board[ni][nj] += amount
                        spread_count += 1

                new_board[i][j] += board[i][j] - amount * spread_count

    return new_board


# 2. 공기청정기 작동
def operate():
    # 위쪽 (반시계 방향)
    # 위로
    for i in range(upper - 1, 0, -1):
        board[i][0] = board[i - 1][0]

    # 왼쪽 -> 오른쪽
    for j in range(c - 1):
        board[0][j] = board[0][j + 1]

    # 아래로
    for i in range(upper):
        board[i][c - 1] = board[i + 1][c - 1]

    # 오른쪽 -> 왼쪽
    for j in range(c - 1, 1, -1):
        board[upper][j] = board[upper][j - 1]

    board[upper][1] = 0

    # 아래쪽 (시계 방향)
    # 아래로
    for i in range(lower + 1, r - 1):
        board[i][0] = board[i + 1][0]

    # 왼쪽 -> 오른쪽
    for j in range(c - 1):
        board[r - 1][j] = board[r - 1][j + 1]

    # 위로
    for i in range(r - 1, lower, -1):
        board[i][c - 1] = board[i - 1][c - 1]

    # 오른쪽 -> 왼쪽
    for j in range(c - 1, 1, -1):
        board[lower][j] = board[lower][j - 1]

    board[lower][1] = 0


# T초 동안 순서대로 반복
for _ in range(t):
    board = spread()
    operate()

# 남은 미세먼지 합 계산
result = 0
for i in range(r):
    for j in range(c):
        if board[i][j] > 0:
            result += board[i][j]

print(result)
