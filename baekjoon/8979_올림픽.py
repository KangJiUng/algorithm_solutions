N, K = map(int, input().split())

medal = {}

for _ in range(N):
    num, g, s, b = map(int, input().split())
    medal[num] = [g, s, b]

# 금, 은, 동 순으로 내림차순 정렬
sorted_medal = sorted(medal.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2]))

rank = 1

for i in range(len(sorted_medal)):
    # 첫 나라는 무조건 1등
    if i == 0:
        if sorted_medal[i][0] == K:
            print(rank)
            break
        continue

    # 앞 나라와 메달 수가 다르면 등수 갱신
    if sorted_medal[i][1] != sorted_medal[i - 1][1]:
        rank = i + 1

    if sorted_medal[i][0] == K:
        print(rank)
        break
