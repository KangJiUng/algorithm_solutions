import sys


def main():
    input_data = sys.stdin.readline

    q = int(input_data())
    ant_location = {}
    next_home_num = 1

    for _ in range(q):
        cmds = list(map(int, input_data().split()))
        cmd = cmds[0]

        if cmd == 100:
            n = cmds[1]

            for i in range(n):
                # key: 개미집 번호 / value: 개미집 위치
                ant_location[next_home_num] = cmds[2 + i]
                next_home_num += 1

        elif cmd == 200:
            # p는 이제까지 건설된 모든 개미집의 좌표보다 큰 값으로 주어짐
            ant_location[next_home_num] = cmds[1]
            next_home_num += 1

        elif cmd == 300:
            del ant_location[cmds[1]]

        elif cmd == 400:
            r = cmds[1]

            active_homes = list(ant_location.values())

            if len(active_homes) == r:
                print(0)
                continue

            left = 0
            right = 10**9
            answer = right

            while left <= right:
                mid = (left + right) // 2
                ants = 0
                cover_end = -1  # 개미가 갈 수 있는 x 좌표 경계
                possible = True

                for p in active_homes:
                    # 현재 집이 기존 개미가 갈 수 있는 범위를 넘어섰다면
                    if p > cover_end:
                        ants += 1  # 정찰개미 추가

                        if ants > r:
                            possible = False
                            break

                        cover_end = (
                            p + mid
                        )  # 투입된 개미가 현재 집 p부터 mid거리만큼 덮음

                if possible:
                    answer = mid
                    right = mid - 1
                else:
                    left = mid + 1

            print(answer)


main()
