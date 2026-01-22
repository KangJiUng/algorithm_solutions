# 풀이 1 - 정확성 53.8, 효율성 테스트 실패
def solution(board, skill):
    answer = 0

    for i in range(len(skill)):
        # 적의 공격
        if skill[i][0] == 1:
            r1, c1 = skill[i][1], skill[i][2]
            r2, c2 = skill[i][3], skill[i][4]

            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    board[r][c] -= skill[i][5]

        # 아군의 회복 스킬
        if skill[i][0] == 2:
            r1, c1 = skill[i][1], skill[i][2]
            r2, c2 = skill[i][3], skill[i][4]

            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    board[r][c] += skill[i][5]

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] > 0:
                answer += 1

    return answer


# 풀이 2 - 누적합 이용(효율성 46.2)
def solution(board, skill):
    answer = 0

    N = len(board)
    M = len(board[0])

    # 누적합 배열(accumulate(누적하다))
    # 범위에서 +1 위치에 기록하므로 M + 1만큼 크게 만듦
    acc = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(len(skill)):
        r1, c1 = skill[i][1], skill[i][2]
        r2, c2 = skill[i][3], skill[i][4]
        degree = skill[i][5]

        # 공격이면 음수로
        if skill[i][0] == 1:
            degree *= -1

        # 4군데에만 변화 기록(꼭짓점)
        acc[r1][c1] += degree
        acc[r1][c2 + 1] -= degree
        acc[r2 + 1][c1] -= degree
        acc[r2 + 1][c2 + 1] += degree

    # 가로 누적합
    for r in range(N):
        # 누적합은 이전 칸의 값을 더하는 연산이므로, 이전 칸이 존재하는 인덱스(1)부터 시작
        for c in range(1, M):
            acc[r][c] += acc[r][c - 1]

    # 세로 누적합
    # 가로 누적만으로는 한 행만 적용되므로, 아래 행들까지 확산시키기 위해 세로 누적 수행
    for c in range(M):
        for r in range(1, N):
            acc[r][c] += acc[r - 1][c]

    # 최종 board 값 계산 + 정답 카운트
    for r in range(N):
        for c in range(M):
            if board[r][c] + acc[r][c] > 0:
                answer += 1

    return answer
