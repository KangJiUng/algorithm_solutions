# AI, 검색 도움

# 풀이 1
import sys


def main():
    input_data = sys.stdin.readline
    line = input_data().split()

    # 입력값이 비어있을 경우를 대비한 안전장치
    if not line:
        return

    n, m = map(int, line)
    grid = [[0] * n for _ in range(n)]
    boxes = {}

    for _ in range(m):
        # 택배 번호 k, 세로 크기 h, 가로 크기 w, 좌측 좌표 c
        k, h, w, c = map(int, input_data().split())
        c -= 1  # 문제에서 주어진 c가 1부터 시작하므로

        # 떨어질 수 있는 가장 아래 행(r) 찾기
        r = 0
        while r + h < n:
            # 내 바로 아래 행(r+h)의 가로 구간(c ~ c+w-1) 중 하나라도 0이 아니면 멈춤
            can_go = True
            for j in range(c, c + w):
                if grid[r + h][j] != 0:
                    can_go = False
                    break

            if not can_go:
                break
            r += 1

        # 투입된 박스 위치 정보 저장(r, c)
        boxes[k] = [r, c, h, w]
        for i in range(r, r + h):
            for j in range(c, c + w):
                grid[i][j] = k

    def falling():
        # 아래쪽에 있는 택배부터 검사해야 하므로 r 기준 내림차순 정렬
        sorted_keys = sorted(boxes.keys(), key=lambda x: boxes[x][0], reverse=True)

        for k in sorted_keys:
            r, c, h, w = boxes[k]

            # 현재 위치 지우기 (자기가 자기 몸에 걸리지 않게)
            for i in range(r, r + h):
                for j in range(c, c + w):
                    grid[i][j] = 0

            # 아래로 최대한 내리기
            new_r = r
            while new_r + h < n:
                can_drop = True
                for j in range(c, c + w):
                    if grid[new_r + h][j] != 0:
                        can_drop = False
                        break

                if not can_drop:
                    break
                new_r += 1

            # 새 위치 기록
            boxes[k][0] = new_r
            for i in range(new_r, new_r + h):
                for j in range(c, c + w):
                    grid[i][j] = k

    def can_unload(k, direction):
        r, c, h, w = boxes[k]

        if direction == "left":
            for i in range(r, r + h):
                # 0부터 c-1 열까지 중 0이 아닌 게 하나라도 있는지 확인
                for j in range(0, c):
                    if grid[i][j] != 0:
                        return False
        else:  # right
            for i in range(r, r + h):
                # c+w부터 n-1 열까지 중 0이 아닌 게 하나라도 있는지 확인
                for j in range(c + w, n):
                    if grid[i][j] != 0:
                        return False
        return True

    ans = []

    # 공간에 있는 택배를 모두 하차할 때까지 2, 3의 과정을 반복
    # 왼쪽 한 번 -> 오른쪽 한 번 -> 왼 -> 오 -> 왼 -> ...
    while boxes:
        # 이번 턴(좌+우)을 시작하기 전, 남은 택배 개수 기억하기!
        prev_box_count = len(boxes)

        # 1. 왼쪽 턴
        left_candidates = [k for k in boxes if can_unload(k, "left")]
        if left_candidates:
            # 가능한 택배 중 번호가 가장 작은 것 선택
            target_k = min(left_candidates)
            ans.append(target_k)

            # 격자 및 딕셔너리에서 지우기
            r, c, h, w = boxes[target_k]
            for i in range(r, r + h):
                for j in range(c, c + w):
                    grid[i][j] = 0
            del boxes[target_k]

            # 하차 발생 시마다 중력 적용
            falling()

        if not boxes:
            break

        # 2. 오른쪽 턴
        right_candidates = [k for k in boxes if can_unload(k, "right")]
        if right_candidates:
            # 가능한 택배 중 번호가 가장 작은 것 선택
            target_k = min(right_candidates)
            ans.append(target_k)

            # 격자 및 딕셔너리에서 지우기
            r, c, h, w = boxes[target_k]
            for i in range(r, r + h):
                for j in range(c, c + w):
                    grid[i][j] = 0
            del boxes[target_k]

            # 하차 발생 시마다 중력 적용
            falling()

        # 3. 무한루프 방지
        if len(boxes) == prev_box_count:
            break

    for i in range(len(ans)):
        print(ans[i])


main()


# 풀이 2(슬라이싱 사용, 15ms 단축)
import sys


def main():
    input_data = sys.stdin.readline
    line = input_data().split()

    n, m = map(int, line)
    grid = [[0] * n for _ in range(n)]
    boxes = {}

    for _ in range(m):
        # 택배 번호 k, 세로 크기 h, 가로 크기 w, 좌측 좌표 c
        k, h, w, c = map(int, input_data().split())
        c -= 1  # 문제에서 주어진 c가 1부터 시작하므로

        # 떨어질 수 있는 가장 아래 행(r) 찾기
        r = 0
        while r + h < n:
            # 내 바로 아래 행(r+h)의 가로 구간(c ~ c+w-1) 중 하나라도 0이 아니면 멈춤
            if any(grid[r + h][c : c + w]):
                break
            r += 1

        # 투입된 박스 위치 정보 저장(r, c)
        boxes[k] = [r, c, h, w]
        for i in range(r, r + h):
            grid[i][c : c + w] = [k] * w

    def falling():
        # 아래쪽에 있는 택배부터 검사해야 하므로 r 기준 내림차순 정렬
        sorted_keys = sorted(boxes.keys(), key=lambda x: boxes[x][0], reverse=True)

        for k in sorted_keys:
            r, c, h, w = boxes[k]

            # 현재 위치 지우기 (자기가 자기 몸에 걸리지 않게)
            for i in range(r, r + h):
                grid[i][c : c + w] = [0] * w

            # 아래로 최대한 내리기
            new_r = r
            while new_r + h < n:
                if any(grid[new_r + h][c : c + w]):
                    break
                new_r += 1

            # 새 위치 기록
            boxes[k][0] = new_r
            for i in range(new_r, new_r + h):
                grid[i][c : c + w] = [k] * w

    def can_unload(k, direction):
        r, c, h, w = boxes[k]

        if direction == "left":
            for i in range(r, r + h):
                # 0부터 c-1 열까지 중 0이 아닌 게 하나라도 있는지
                if any(grid[i][:c]):
                    return False
        else:  # right
            for i in range(r, r + h):
                # c+w부터 n-1 열까지 중 0이 아닌 게 하나라도 있는지
                if any(grid[i][c + w :]):
                    return False
        return True

    ans = []

    while boxes:
        prev_box_count = len(boxes)

        left_candidates = [k for k in boxes if can_unload(k, "left")]

        if left_candidates:
            target_k = min(left_candidates)
            ans.append(target_k)

            r, c, h, w = boxes[target_k]
            for i in range(r, r + h):
                grid[i][c : c + w] = [0] * w
            del boxes[target_k]

            falling()

        if not boxes:
            break

        right_candidates = [k for k in boxes if can_unload(k, "right")]

        if right_candidates:
            target_k = min(right_candidates)
            ans.append(target_k)

            r, c, h, w = boxes[target_k]
            for i in range(r, r + h):
                grid[i][c : c + w] = [0] * w
            del boxes[target_k]

            falling()

        if len(boxes) == prev_box_count:
            break

    for i in range(len(ans)):
        print(ans[i])


main()
