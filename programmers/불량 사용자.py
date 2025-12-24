def is_match(user, banned):
    if len(user) != len(banned):
        return False

    for u, b in zip(user, banned):
        if b == "*":
            continue
        if u != b:
            return False

    return True


# 검색 도움
# 불량 사용자에 매핑되는 제재 아이디의 목록 경우의 수를 구해야함
# idx: 현재 처리 중인 banned_id의 인덱스
# candidates: banned_id마다 가능한 user_id 후보 리스트
# chosen: 지금까지 선택한 user_id들(같은 user_id 중복 선택 방지 역할)
# result: 최종 정답 저장(순서 무시, 중복 결과 제거)
def dfs(idx, candidates, chosen, result):
    # len(candidates) = len(banned_id)
    if idx == len(candidates):
        result.add(frozenset(chosen))
        return

    # 현재 banned_id(idx)에 대해 가능한 user 후보들을 하나씩 시도
    for user in candidates[idx]:
        # 이미 이전 banned_id에서 사용한 user면 불가능 조합
        if user in chosen:
            continue

        chosen.add(user)
        dfs(idx + 1, candidates, chosen, result)

        # 백트래킹(해당 유저는 끝)
        chosen.remove(user)


def solution(user_id, banned_id):
    answer = 0
    candidates = []

    for b_id in banned_id:
        temp = []

        for u_id in user_id:
            if is_match(u_id, b_id):
                temp.append(u_id)

        candidates.append(temp)

    result = set()
    dfs(0, candidates, set(), result)

    return len(result)
