from itertools import combinations
from collections import deque
import copy

# 입력
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 빈 칸과 바이러스 위치 저장
empty = []
virus = []

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_safe = 0

# 빈 칸 중 3개를 선택
for walls in combinations(empty, 3):

    # 지도 복사
    temp = copy.deepcopy(lab)

    # 벽 세우기
    for x, y in walls:
        temp[x][y] = 1

    # BFS로 바이러스 확산
    queue = deque(virus)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx, ny))

    # 안전 영역 계산
    safe = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safe += 1

    max_safe = max(max_safe, safe)

print(max_safe)
