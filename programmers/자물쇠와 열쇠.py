def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 예외처리 - 열쇠의 돌기 부분이 자물쇠의 홈보다 적어서 열 수 없음
    if sum(k.count(1) for k in key) < sum(l.count(0) for l in lock):
        return False
    # 예외처리 - 자물쇠의 홈이 없음(모든 홈이 다 채워져있음)
    if sum(l.count(0) for l in lock) == 0:
        return True

    # 확장 보드 (3n x 3n)
    board = [[0] * (3 * n) for _ in range(3 * n)]

    # 자물쇠를 가운데(n, n)부터 배치
    for i in range(n):
        for j in range(n):
            board[n + i][n + j] = lock[i][j]

    # 4번 회전
    for _ in range(4):
        # 시계 방향 90도 회전 (* - 언패킹)
        key = list(zip(*key[::-1]))

        # 열쇠 이동
        for x in range(2 * n):
            for y in range(2 * n):

                # 열쇠 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        board[x + i][y + j] += key[i][j]

                # 자물쇠 영역 검사
                opened = True
                for i in range(n):
                    for j in range(n):
                        if board[n + i][n + j] != 1:
                            opened = False
                            break
                    if not opened:
                        break

                if opened:
                    return True

                # 원상 복구
                for i in range(m):
                    for j in range(m):
                        board[x + i][y + j] -= key[i][j]

    return False
