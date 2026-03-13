# .이라면 (i, j) 위치에는 안전한 돌
# S라면 미끄러운 돌
# #이라면 천적이 사는 돌

# 각 여행에 걸리는 최소 시간을 출력

import sys
import heapq

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
INF = 10**18


def solution(n, lake, r1, c1, r2, c2):
    dist = [[[INF] * 6 for _ in range(n)] for _ in range(n)]
    pq = []

    # 각 여행의 초기 점프력은 항상 1
    dist[r1][c1][1] = 0
    heapq.heappush(pq, (0, r1, c1, 1))

    while pq:
        # (현재까지 시간, 행, 열, 점프력)
        t, r, c, k = heapq.heappop(pq)

        # 걸리는 시간이 있던 거보다 오래걸리면 넘김
        if dist[r][c][k] < t:
            continue

        # 현재 위치가 도착점이면 바로 반환
        if r == r2 and c == c2:
            return t

        # 점프
        for d in range(4):
            nr = r + dr[d] * k
            nc = c + dc[d] * k

            if not (0 <= nr < n and 0 <= nc < n):
                continue

            possible = True

            # 현재 위치에서 도착점까지 한 칸씩 이동해봄
            for step in range(1, k + 1):
                cur_r = r + dr[d] * step
                cur_c = c + dc[d] * step

                # 천적이 사는 돌
                if lake[cur_r][cur_c] == "#":
                    possible = False
                    break

            # 미끄러운 돌
            if possible and lake[nr][nc] == "S":
                possible = False

            if possible:
                nt = t + 1
                if dist[nr][nc][k] > nt:
                    dist[nr][nc][k] = nt
                    heapq.heappush(pq, (nt, nr, nc, k))

        # 점프력 증가
        if k < 5:
            nk = k + 1
            nt = t + nk * nk
            if dist[r][c][nk] > nt:
                dist[r][c][nk] = nt
                heapq.heappush(pq, (nt, r, c, nk))

        # 점프력 감소
        for nk in range(1, k):
            nt = t + 1
            if dist[r][c][nk] > nt:
                dist[r][c][nk] = nt
                heapq.heappush(pq, (nt, r, c, nk))

    return -1


if __name__ == "__main__":
    n = int(input())
    lake = [input().strip() for _ in range(n)]
    q = int(input())

    for _ in range(q):
        r1, c1, r2, c2 = map(int, input().split())

        # (0, 0) 시작으로 맞춤
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1

        print(solution(n, lake, r1, c1, r2, c2))
