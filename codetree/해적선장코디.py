# 풀이 1 - 시간 초과(완전 탐색)
def main():
    t = int(input())

    ships = {}

    def add_ship(ship_id, p, r):
        ships[ship_id] = [p, r, 0]

    def change_ship(ship_id, new_p):
        if ship_id in ships:
            old_r = ships[ship_id][1]
            old_time = ships[ship_id][2]
            ships[ship_id] = [new_p, old_r, old_time]

    def attack(current_time):
        # 1. '사격 대기' 상태인 배들만 (현재 시간이 사격 가능 시간보다 크거나 같아야 함)
        ready_ships = []
        for ship_id, info in ships.items():
            if info[2] <= current_time:
                ready_ships.append((ship_id, info))

        # 2. 문제 조건에 맞춰 정렬
        # 사격 대기 상태인 선박 중 공격력이 가장 높은 선박
        # 공격력이 같다면 선박 번호 id가 작은 선박을 우선 선택
        # info[0]은 공격력(p) -> 내림차순이어야하므로 -를 붙임
        ready_ships.sort(key=lambda x: (-x[1][0], x[0]))

        # 3. 최대 5척만
        top_5_ships = ready_ships[:5]

        # 사격 가능한 배가 한 척도 없는 경우 예외 처리
        if not top_5_ships:
            return "0 0"

        total_attack = 0
        attacked_ids = []

        for ship_id, info in top_5_ships:
            total_attack += info[0]
            # 해당 배는 사격했으므로 쿨타임 갱신 (현재 시간 + r)
            info[2] = current_time + info[1]

            # 문자열 출력을 위해 id를 문자열로 변환하여 리스트에 추가
            attacked_ids.append(str(ship_id))

        # 4. 반환
        return f"{total_attack} {len(attacked_ids)} " + " ".join(attacked_ids)

    # 각 명령은 1시간 단위로 실행 -> t == 사격 시간
    for time_step in range(1, t + 1):
        cmds = list(map(int, input().split()))
        cmd = cmds[0]

        if cmd == 100:
            n = cmds[1]
            for i in range(2, 2 + n * 3, 3):
                ship_id = cmds[i]
                p = cmds[i + 1]
                r = cmds[i + 2]
                ships[ship_id] = [p, r, 0]

        elif cmd == 200:
            add_ship(cmds[1], cmds[2], cmds[3])

        elif cmd == 300:
            change_ship(cmds[1], cmds[2])

        elif cmd == 400:
            print(attack(time_step))


main()


# 풀이 2 - sys, heapq(우선순위 큐) 사용
import sys
import heapq


def main():
    input = sys.stdin.read().split()
    if not input:
        return

    t = int(input[0])
    idx = 1  # input 읽을 인덱스 포인터

    ships = {}

    # 사격 가능한 배들
    ready_ships = []

    # 사격 불가능 배들(쿨타임)
    cooldown_ships = []

    def add_ship(ship_id, p, r):
        ships[ship_id] = [p, r, 0]
        # -p로 넣어서 최대힙 이용
        heapq.heappush(ready_ships, (-p, ship_id))

    def change_ship(ship_id, new_p):
        if ship_id in ships:
            ships[ship_id][0] = new_p  # 공격력만 갱신

            if ships[ship_id][2] <= time_step:
                heapq.heappush(ready_ships, (-new_p, ship_id))

    def attack(current_time):
        # 1. 쿨타임이 끝난 배들을 ready_pq로 복귀
        while cooldown_ships and cooldown_ships[0][0] <= current_time:
            ready_time, ship_id = heapq.heappop(cooldown_ships)
            # 최신 쿨타임 기록과 일치하는지 확인
            if ships[ship_id][2] == ready_time:
                # 쿨타임 끝남 -> 최신 공격력으로 큐에 투입
                heapq.heappush(ready_ships, (-ships[ship_id][0], ship_id))

        # 2. 최대 5척 고르기
        total_attack = 0
        attacked_ids = []

        # ready_pq에서 5척을 뽑을 때까지 반복
        # 대기열에 배가 5척보다 적으면 그만큼 돌고 끝남(최대 5척)
        while ready_ships and len(attacked_ids) < 5:
            # 공격력 가장 높은 배를 꺼냄
            neg_p, ship_id = heapq.heappop(ready_ships)

            # 방금 뽑은 공격력(-neg_p)이 진짜 최신 공격력인지 확인
            # 이 배가 현재 장전이 끝난 상태가 맞는지 확인(if문 조건 true면 공격 가능)
            # 공격력 같은지 and 쿨타임 다 끝난 거 맞는지
            if ships[ship_id][0] == -neg_p and ships[ship_id][2] <= current_time:
                total_attack += -neg_p
                attacked_ids.append(str(ship_id))

                # 3. 사격했으므로 쿨타임 갱신 후 cooldown_ships로 보냄
                ships[ship_id][2] = current_time + ships[ship_id][1]
                heapq.heappush(cooldown_ships, (ships[ship_id][2], ship_id))

        # 4. 반환 (사격한 배가 0척인 경우 처리)
        if not attacked_ids:
            return "0 0"

        return f"{total_attack} {len(attacked_ids)} " + " ".join(attacked_ids)

    # 각 명령은 1시간 단위로 실행 -> t == 사격 시간
    for time_step in range(1, t + 1):
        cmd = int(input[idx])

        if cmd == 100:
            n = int(input[idx + 1])
            idx += 2  # n까지 읽었으므로 2칸 전진

            for _ in range(n):
                ship_id = int(input[idx])
                p = int(input[idx + 1])
                r = int(input[idx + 2])
                add_ship(ship_id, p, r)
                idx += 3  # 한 척 정보 읽을 때마다 3칸 전진

        elif cmd == 200:
            add_ship(int(input[idx + 1]), int(input[idx + 2]), int(input[idx + 3]))
            idx += 4

        elif cmd == 300:
            change_ship(int(input[idx + 1]), int(input[idx + 2]))
            idx += 3

        elif cmd == 400:
            print(attack(time_step))
            idx += 1


main()
