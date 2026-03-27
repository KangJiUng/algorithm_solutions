from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1

    # 원형 -> 일자 형태로 펼치기
    weak_extended = weak + [w + n for w in weak]

    # 각 취약 지점을 시작점으로 시도
    for start in range(len(weak)):
        for friends in permutations(dist, len(dist)):
            count = 1  # 현재 투입한 친구 수

            # 첫 번째 친구가 커버 가능한 마지막 위치
            position = weak_extended[start] + friends[count - 1]

            # 시작점부터 weak 취약지점 확인
            for idx in range(start, start + len(weak)):
                # 현재 친구가 못 덮는 지점이면 다음 친구 투입
                if weak_extended[idx] > position:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak_extended[idx] + friends[count - 1]

            answer = min(answer, count)

    if answer > len(dist):
        return -1

    return answer
