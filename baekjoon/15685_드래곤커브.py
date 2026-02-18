n = int(input())
grid = [[0] * 101 for _ in range(101)]

# 방향
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    x, y, d, g = map(int, input().split())

    directions = [d]

    for _ in range(g):
        # 끝점 기준으로 이어 붙여야함 -> 역순 이용
        for direction in reversed(directions):
            # 90도씩 회전
            # 방향 0, 1, 2, 3에서 3 -> 4 나오면 0으로 설정
            directions.append((direction + 1) % 4)

    # 시작점 표시
    grid[y][x] = 1

    # 이동하면서 점 찍기
    for direction in directions:
        x += dx[direction]
        y += dy[direction]
        grid[y][x] = 1

# 정사각형 개수 세기
count = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i][j + 1] and grid[i + 1][j] and grid[i + 1][j + 1]:
            count += 1

print(count)
