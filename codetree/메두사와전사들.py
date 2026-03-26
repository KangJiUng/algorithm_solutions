# 해설, AI 참고

import sys
from collections import deque

# 방향 우선순위 정의
P1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 (메두사 & 전사 1차 이동)
P2 = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 좌우상하 (전사 2차 이동)

# 시야(90도) 3갈래 벡터: 위/아래/좌/우
VISION_DXYS = [
    [(-1, -1), (-1, 0), (-1, 1)],  # 위
    [(1, -1), (1, 0), (1, 1)],  # 아래
    [(-1, -1), (0, -1), (1, -1)],  # 좌
    [(-1, 1), (0, 1), (1, 1)],  # 우
]


def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N


def manhattan(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)


class WarriorMap:
    """전사 배열 + 칸별 전사 인덱스 집합 관리. pop-back swap으로 O(1) 삭제 수행."""

    __slots__ = ("N", "warriors", "cells")

    def __init__(self, N, init_warriors):
        self.N = N
        self.warriors = list(init_warriors)
        self.cells = [[set() for _ in range(N)] for __ in range(N)]
        for i, (x, y) in enumerate(self.warriors):
            self.cells[x][y].add(i)

    def remove_warrior(self, idx):
        x, y = self.warriors[idx]
        self.cells[x][y].discard(idx)
        last = len(self.warriors) - 1
        if idx != last:
            self.warriors[idx] = self.warriors[last]
            rx, ry = self.warriors[idx]
            self.cells[rx][ry].discard(last)
            self.cells[rx][ry].add(idx)
        self.warriors.pop()

    def remove_same_cell(self, mx, my):
        removed = 0
        i = 0
        while i < len(self.warriors):
            if self.warriors[i][0] == mx and self.warriors[i][1] == my:
                self.remove_warrior(i)
                removed += 1
            else:
                i += 1
        return removed

    def move_warrior_once(self, idx, mx, my, vision_map, pri):
        x, y = self.warriors[idx]
        d0 = manhattan(x, y, mx, my)
        for dx, dy in pri:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, self.N) and vision_map[nx][ny] == 0:
                if manhattan(nx, ny, mx, my) < d0:
                    self.cells[x][y].discard(idx)
                    self.warriors[idx] = (nx, ny)
                    self.cells[nx][ny].add(idx)
                    return 1
        return 0

    def warriors_move(self, vision_map, mx, my):
        # 1. 메두사 이동 직후 같은 칸 전사 제거
        self.remove_same_cell(mx, my)

        steps_sum = 0
        i = 0
        while i < len(self.warriors):
            x, y = self.warriors[i]
            # 석화되지 않은 전사만 이동
            if vision_map[x][y] == 0:
                steps_sum += self.move_warrior_once(i, mx, my, vision_map, P1)
                steps_sum += self.move_warrior_once(i, mx, my, vision_map, P2)
            i += 1

        # 2. 전사 이동 종료 후 메두사 공격 전사 제거 및 수 반환
        attackers = self.remove_same_cell(mx, my)
        return steps_sum, attackers


def get_vision_map(N, wmap, mx, my, dxys3):
    vision = [[0] * N for _ in range(N)]
    seen_cnt = 0
    vis_q = deque()

    # 1) 표시 BFS: 3갈래로 시야 확장
    q = deque([(mx, my)])
    while q:
        x, y = q.popleft()
        for dxi, dyi in dxys3:
            nx, ny = x + dxi, y + dyi
            if in_range(nx, ny, N) and vision[nx][ny] == 0:
                if len(wmap.cells[nx][ny]) > 0:
                    # 갈래 타입 판정 (좌대각 0, 직선 1, 우대각 2)
                    if nx == mx or ny == my:
                        t = 1
                    else:
                        t = (
                            0
                            if (nx - mx) * dxys3[0][0] > 0
                            and (ny - my) * dxys3[0][1] > 0
                            else 2
                        )
                    vis_q.append((nx, ny, t))
                vision[nx][ny] = 1
                q.append((nx, ny))

    # 2) 가림 BFS: 전사 뒤쪽 가리기
    while vis_q:
        x, y, t = vis_q.popleft()
        for d, (dxi, dyi) in enumerate(dxys3):
            if (t == 1 and d != 1) or (t == 0 and d == 2) or (t == 2 and d == 0):
                continue
            nx, ny = x + dxi, y + dyi
            if in_range(nx, ny, N) and vision[nx][ny] == 1:
                vision[nx][ny] = 0
                vis_q.append((nx, ny, t))

    # 3) 최종 석화된 전사 수 집계
    for i in range(N):
        row_cells = wmap.cells[i]
        v_row = vision[i]
        for j in range(N):
            if v_row[j]:
                seen_cnt += len(row_cells[j])
    return vision, seen_cnt


def get_medusa_dist(N, road, ex, ey):
    dist = [[-1] * N for _ in range(N)]
    q = deque([(ex, ey)])
    dist[ex][ey] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in P1:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, N) and road[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist


def solution():
    # 고속 입력 처리
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)

    N, M = int(next(it)), int(next(it))
    sx, sy, ex, ey = int(next(it)), int(next(it)), int(next(it)), int(next(it))

    init_warriors = []
    for _ in range(M):
        init_warriors.append((int(next(it)), int(next(it))))

    road = [[int(next(it)) for _ in range(N)] for _ in range(N)]

    # 1. 메두사 최단 경로 전처리
    dist_map = get_medusa_dist(N, road, ex, ey)
    if dist_map[sx][sy] == -1:
        print("-1")
        return

    wmap = WarriorMap(N, init_warriors)
    mx, my = sx, sy
    output = []

    # 2. 메두사가 공원에 도착할 때까지 반복
    while (mx, my) != (ex, ey):
        # [1] 메두사 한 칸 이동 (상-하-좌-우 우선순위)
        for dx, dy in P1:
            nx, ny = mx + dx, my + dy
            if (
                in_range(nx, ny, N)
                and dist_map[nx][ny] != -1
                and dist_map[nx][ny] == dist_map[mx][my] - 1
            ):
                mx, my = nx, ny
                break

        if (mx, my) == (ex, ey):
            output.append("0")
            break

        # [2] 메두사 시선 결정 (가장 많은 전사를 볼 수 있는 방향 선택)
        best_seen = -1
        best_vision = None
        for d in range(4):
            v_map, seen = get_vision_map(N, wmap, mx, my, VISION_DXYS[d])
            if seen > best_seen:
                best_seen = seen
                best_vision = v_map

        # [3] 전사들의 이동 및 공격 처리
        moves, attackers = wmap.warriors_move(best_vision, mx, my)
        output.append(f"{moves} {best_seen} {attackers}")

    # 최종 결과 한꺼번에 출력
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    solution()
