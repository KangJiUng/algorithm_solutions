a = list(map(int, input().strip()))
b = list(map(int, input().strip()))
c = list(map(int, input().strip()))
d = list(map(int, input().strip()))
k = int(input())
score = 0

gears = [a, b, c, d]

for i in range(k):
    num, dir = map(int, input().split())
    num -= 1  # 인덱스 맞추기
    rotate = [0, 0, 0, 0]  # 회전 방향 저장
    rotate[num] = dir

    # 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향
    # 맞닿은 톱니의 극이 다르면 회전, 아니면 그대로
    # 왼쪽 전파
    for i in range(num, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            rotate[i - 1] = -rotate[i]
        else:
            break

    # 오른쪽 전파
    # i + 1 비교함에 주의 -> 범위 3까지
    for i in range(num, 3):
        if gears[i][2] != gears[i + 1][6]:
            rotate[i + 1] = -rotate[i]
        else:
            break

    # 실제 회전
    for i in range(4):
        if rotate[i] == 1:  # 시계
            gears[i] = [gears[i][-1]] + gears[i][:-1]
        elif rotate[i] == -1:  # 반시계
            gears[i] = gears[i][1:] + [gears[i][0]]


if gears[0][0] == 1:
    score += 1
if gears[1][0] == 1:
    score += 2
if gears[2][0] == 1:
    score += 4
if gears[3][0] == 1:
    score += 8

print(score)
