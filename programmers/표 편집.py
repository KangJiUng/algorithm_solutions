# "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택
# "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택
# "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택
# 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택
# "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
# 표의 범위를 벗어나는 이동은 입력으로 주어지지 않습니다.


def solution(n, k, cmd):
    answer = ""
    state = [True for _ in range(n)]
    stack = []

    prev = [i - 1 for i in range(n)]
    next = [i + 1 for i in range(n)]
    next[n - 1] = -1  # 마지막 행 표시

    for c in cmd:
        if len(c) > 1:
            string, num = c.split()
            num = int(num)
        else:
            string = c

        # 위의 행 선택
        if string == "U":
            for _ in range(num):
                k = prev[k]

        # 아래 행 선택
        if string == "D":
            for _ in range(num):
                k = next[k]

        # 현재 행 삭제
        if string == "C":
            state[k] = False
            stack.append(k)

            # 연결 끊기
            if prev[k] != -1:
                next[prev[k]] = next[k]
            if next[k] != -1:
                prev[next[k]] = prev[k]

            # 커서 이동
            if next[k] != -1:
                k = next[k]
            else:
                k = prev[k]

        # 최근 삭제된 행 복구
        if string == "Z":
            row = stack.pop()
            state[row] = True

            # 연결 복구
            if prev[row] != -1:
                next[prev[row]] = row
            if next[row] != -1:
                prev[next[row]] = row

    for s in state:
        if s:
            answer += "O"
        else:
            answer += "X"

    return answer
