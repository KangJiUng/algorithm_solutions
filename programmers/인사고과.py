def solution(scores):
    # (원래 번호, 근무 태도 점수, 동료 평가 점수)
    people = []
    for i in range(len(scores)):
        a, b = scores[i]
        people.append((i, a, b))

    wanho_a, wanho_b = scores[0]
    wanho_total = wanho_a + wanho_b

    # 완호 탈락 여부 먼저 확인
    for i, a, b in people[1:]:
        if a > wanho_a and b > wanho_b:
            return -1

    # 첫 점수 내림차순, 같으면 둘째 점수 오름차순
    # 같은 첫 점수끼리는 서로 탈락 판정을 내리면 안 되니까 둘째 점수 낮은 사람부터
    people.sort(key=lambda x: (-x[1], x[2]))

    answer = 1
    max_b = 0

    for idx, a, b in people:
        # 인센티브 제외 대상
        if b < max_b:
            continue

        # 완호보다 총점이 높으면 완호 등수 밀림
        if a + b > wanho_total:
            answer += 1

        max_b = max(max_b, b)

    return answer
