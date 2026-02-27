# 1번 칸이 있는 위치를 "올리는 위치", N번 칸이 있는 위치를 "내리는 위치"
# 종료되었을 때 몇 번째 단계가 진행 중이었는지(1~4 순서 다 한 게 한 단계)
# 로봇은 올리는 위치에만 올릴 수 있다. 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다.

n, k = map(int, input().split())
a = list(map(int, input().split()))

robots = [False] * n
step = 0

while True:
    step += 1

    # 벨트 회전
    a = [a[-1]] + a[:-1]
    robots = [False] + robots[:-1]
    robots[-1] = False  # 내리는 위치 로봇 제거

    # 로봇 이동 (뒤에서부터)
    # 그림은 1이 올리는 위치, n이 내리는 위치지만 index 고려 -> 0 / n-1 -> n-2까지 로봇 이동
    for i in range(n - 2, -1, -1):
        if robots[i] and not robots[i + 1] and a[i + 1] > 0:
            robots[i] = False
            robots[i + 1] = True
            a[i + 1] -= 1

    robots[-1] = False  # 내리는 위치 제거

    # 로봇 올리기(내구도 확인)
    if a[0] > 0:
        robots[0] = True
        a[0] -= 1

    if a.count(0) >= k:
        break

print(step)
