n = int(input())
room = [[0] * n for _ in range(n)]
like = dict()
total = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n * n):
    row = list(map(int, input().split()))
    key = row[0]
    value = row[1:]
    like[key] = value

for key in like:
    candidates = []

    for x in range(n):
        for y in range(n):
            if room[x][y] == 0:
                like_cnt = 0
                empty_cnt = 0

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < n and 0 <= ny < n:
                        if room[nx][ny] in like[key]:
                            like_cnt += 1
                        if room[nx][ny] == 0:
                            empty_cnt += 1

                # 행, 열이 작을수록 조건에 해당하므로 -x, -y로 넣기
                candidates.append((like_cnt, empty_cnt, -x, -y))

    # 영향 큰 순으로
    candidates.sort(reverse=True)
    # 제일 처음 후보 위치가 조건에 가장 많이 맞는 위치(언패킹)
    _, _, x, y = candidates[0]
    # candidates에 -x, -y로 들어가있으므로 원상태로 복구
    room[-x][-y] = key

for x in range(n):
    for y in range(n):
        satisfaction = 0

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if room[nx][ny] in like[room[x][y]]:
                    satisfaction += 1

        if satisfaction == 1:
            total += 1
        elif satisfaction == 2:
            total += 10
        elif satisfaction == 3:
            total += 100
        elif satisfaction == 4:
            total += 1000

print(total)
