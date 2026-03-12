# AI, 검색 도움
# r, c를 쓸 때는 행/열 개념과 x, y 좌표가 헷갈려 루프 순서가 꼬였으나,
# x, y로 명칭을 통일하면서 'for x: for y:' 순서로 배치 로직을 작성

import sys
from collections import deque

input = sys.stdin.readline


def get_cells(grid, n, micro_id):
    """특정 미생물 ID가 차지하고 있는 모든 좌표 리스트를 반환"""
    cells = []

    for r in range(n):
        for c in range(n):
            if grid[r][c] == micro_id:
                cells.append((r, c))

    return cells


def is_connected(grid, n, micro_id, cells):
    """해당 미생물의 남은 조각들이 여전히 하나로 연결되어 있는지 확인 (BFS)"""
    if not cells:
        return True

    q = deque([cells[0]])
    visited = {cells[0]}
    count = 1  # 연결해서 도달한 칸 수

    while q:
        r, c = q.popleft()

        # 오른쪽, 왼쪽, 아래, 위를 탐색
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            # 격자 안이고 같은 미생물 ID이며 아직 방문 안 했으면
            if (
                0 <= nr < n
                and 0 <= nc < n
                and grid[nr][nc] == micro_id
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                q.append((nr, nc))
                count += 1

    # 처음 시작한 칸에서 BFS로 도달한 칸 수가 실제로 남아 있는 전체 칸 수와 같으면 모두 연결되어 있다는 뜻
    return count == len(cells)


def solution(n, q):
    grid = [[0] * n for _ in range(n)]

    # 각 미생물별 투입 시간(ID) 저장용
    for current_id in range(1, q + 1):
        r1, c1, r2, c2 = map(int, input().split())

        # 1. 미생물 투입 및 영향받은 미생물 식별
        # 새 미생물이 덮어쓴 기존 미생물만 검사하기 위함
        impacted_ids = set()
        for x in range(r1, r2):
            for y in range(c1, c2):
                if grid[x][y] != 0:
                    impacted_ids.add(grid[x][y])
                grid[x][y] = current_id

        # 2. 잘려나간 미생물들의 분리 판정 및 소멸 처리
        for micro_id in impacted_ids:
            remaining = get_cells(grid, n, micro_id)

            if not is_connected(grid, n, micro_id, remaining):
                for rr, cc in remaining:
                    grid[rr][cc] = 0

        # 3. 배양 용기 이동 (재배치)
        active_groups = []
        present_ids = set()

        for row in grid:
            for cell in row:
                if cell != 0:
                    present_ids.add(cell)

        present_ids = sorted(present_ids)

        for micro_id in present_ids:
            m_cells = get_cells(grid, n, micro_id)

            # x 최소 → y 최소 위치에 배치 (c → r 순서 탐색)
            # 그림상 좌하단이지만
            # 배열은 이렇게 생김
            # r=0  (0,0) (0,1) (0,2)
            # r=1  (1,0) (1,1) (1,2)
            # r=2  (2,0) (2,1) (2,2)
            # 방향: r 증가 ↓, c 증가 →
            # 그래서
            # r 작은 값 = 위
            # r 큰 값 = 아래
            min_r = min(c[0] for c in m_cells)
            min_c = min(c[1] for c in m_cells)

            # 모양을 상대좌표로 바꾸는 코드
            shape = [(r - min_r, c - min_c) for r, c in m_cells]
            active_groups.append({"id": micro_id, "area": len(m_cells), "shape": shape})

        # 정렬: 면적 내림차순, ID 오름차순
        active_groups.sort(key=lambda x: (-x["area"], x["id"]))

        new_grid = [[0] * n for _ in range(n)]
        final_placed_ids = {}  # 실제로 배치 성공한 미생물만 저장하는 저장소 추가

        for group in active_groups:
            placed = False
            # 조건: x좌표(c) 최소 -> y좌표(r) 최소 (문제 기준)
            for x in range(n):
                for y in range(n):
                    can_place = True

                    # 미생물을 새 위치로 옮길 수 있는지 확인
                    for dx, dy in group["shape"]:
                        nx, ny = x + dx, y + dy
                        if not (0 <= nx < n and 0 <= ny < n and new_grid[nx][ny] == 0):
                            can_place = False
                            break

                    if can_place:
                        for dx, dy in group["shape"]:
                            new_grid[x + dx][y + dy] = group["id"]

                        # 배치에 성공했을 때만 면적 정보를 기록함
                        final_placed_ids[group["id"]] = group["area"]
                        placed = True
                        break
                if placed:
                    break

        grid = new_grid  # 배치 완료된 격자로 업데이트

        # 4. 실험 결과 기록 (인접 무리 점수 계산)
        score = 0
        adj_pairs = set()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                id1 = grid[r][c]

                for dr, dc in [(0, 1), (1, 0)]:  # 중복 방지를 위해 아래와 오른쪽만 체크
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < n
                        and 0 <= nc < n
                        and grid[nr][nc] != 0
                        and grid[nr][nc] != id1
                    ):
                        pair = tuple(sorted((id1, grid[nr][nc])))
                        adj_pairs.add(pair)

        for id_a, id_b in adj_pairs:
            # final_placed_ids에 있는(배치 성공한) 애들끼리의 점수만 더함
            if id_a in final_placed_ids and id_b in final_placed_ids:
                score += final_placed_ids[id_a] * final_placed_ids[id_b]

        print(score)


if __name__ == "__main__":
    n, q = map(int, input().split())

    solution(n, q)
