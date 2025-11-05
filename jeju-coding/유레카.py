import numpy as np

cross = [
    [
        [1, 5, 0, 1, 0],
        [0, 1, 6, 7, 0],
        [6, 2, 3, 2, 1],
        [1, 0, 1, 1, 1],
        [0, 2, 0, 1, 0],
    ],
    [
        [0, 3, 0, 1, 0],
        [1, 2, 5, 4, 4],
        [0, 0, 3, 0, 0],
        [1, 2, 5, 0, 1],
        [0, 0, 0, 0, 0],
    ],
    [
        [3, 0, 1, 1, 8],
        [5, 0, 4, 5, 4],
        [1, 5, 0, 5, 1],
        [1, 2, 1, 0, 1],
        [0, 2, 5, 1, 1],
    ],
    [
        [1, 0, 3, 3, 3],
        [5, 1, 2, 2, 4],
        [1, 5, 1, 2, 4],
        [4, 4, 1, 1, 1],
        [4, 4, 1, 1, 1],
    ],
    [
        [1, 2, 0, 3, 3],
        [1, 2, 0, 2, 4],
        [1, 2, 0, 2, 4],
        [4, 2, 0, 0, 1],
        [8, 4, 1, 1, 0],
    ],
    [
        [1, 0, 3, 0, 0],
        [1, 1, 0, 2, 4],
        [0, 0, 1, 2, 4],
        [4, 0, 1, 0, 1],
        [0, 0, 1, 0, 1],
    ],
]

# 사분면 제한
#  1. 2사분면 → 4사분면
#  2. 2사분면 → 1사분면 → 4사분면
#  3. 2사분면 → 0사분면 → 5사분면 → 4사분면


# 2사분면 → 4사분면
cross1 = cross[2] + cross[4]

가중치누적값 = [[0 for i in range(5)] for i in range(len(cross1))]
좌표저장 = [[[0, 0] for i in range(5)] for j in range(len(cross1))]

for i in range(len(cross1)):
    for j in range(4, -1, -1):
        if i == 0 and j == 4:
            가중치누적값[0][4] = cross1[0][4]
            좌표저장[i][j] = [99, 99]
        elif i == 0:
            가중치누적값[i][j] = 가중치누적값[i][j + 1] + cross1[i][j]
            좌표저장[i][j] = [i, j + 1]
        elif j == 4:
            가중치누적값[i][j] = 가중치누적값[i - 1][j] + cross1[i][j]
            좌표저장[i][j] = [i - 1, j]
        else:
            if 가중치누적값[i][j + 1] > 가중치누적값[i - 1][j]:
                가중치누적값[i][j] = 가중치누적값[i - 1][j] + cross1[i][j]
                좌표저장[i][j] = [i - 1, j]
            else:
                가중치누적값[i][j] = 가중치누적값[i][j + 1] + cross1[i][j]
                좌표저장[i][j] = [i, j + 1]

i, j = len(cross1) - 1, 0
경로 = []

while not (i == 99 and j == 99):
    경로.append((i, j))
    i, j = 좌표저장[i][j]
경로.reverse()

print("2사분면 -> 4사분면 경로: ", 경로)


# 2사분면 → 1사분면 → 4사분면
# 2사분면 → 1사분면 먼저
# 넘파이는 리스트를 넘파이 배열로 바꿔서 돌린 다음, 그 결과를 ndarray로 반환 -> 요소끼리 더해짐
cross2 = np.rot90(cross[2], 1).tolist() + np.rot90(cross[1], 1).tolist()

가중치누적값 = [[0 for i in range(5)] for i in range(len(cross2))]
좌표저장 = [[[0, 0] for i in range(5)] for j in range(len(cross2))]

for i in range(len(cross2)):
    for j in range(5):
        if i == 0 and j == 0:
            가중치누적값[0][0] = cross2[0][0]
            좌표저장[i][j] = [99, 99]
        elif i == 0:
            가중치누적값[i][j] = 가중치누적값[i][j - 1] + cross2[i][j]
            좌표저장[i][j] = [i, j - 1]
        elif j == 0:
            가중치누적값[i][j] = 가중치누적값[i - 1][j] + cross2[i][j]
            좌표저장[i][j] = [i - 1, j]
        else:
            if 가중치누적값[i - 1][j] > 가중치누적값[i][j - 1]:
                가중치누적값[i][j] = 가중치누적값[i - 1][j] + cross2[i][j]
                좌표저장[i][j] = [i - 1, j]
            else:
                가중치누적값[i][j] = 가중치누적값[i][j - 1] + cross2[i][j]
                좌표저장[i][j] = [i, j - 1]


i, j = len(cross2) - 1, 4
경로 = []

while not (i == 99 and j == 99):
    경로.append((i, j))
    i, j = 좌표저장[i][j]

경로.reverse()

print("2사분면 -> 1사분면 경로: ", 경로)


# 1사분면 → 4사분면
cross_1 = cross[1]
cross_4 = np.rot90(cross[4], -1).tolist()
cross2 = cross_1[4] + cross_4[0]
