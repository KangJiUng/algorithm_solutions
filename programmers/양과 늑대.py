def solution(info, edges):
    answer = 0
    tree = [[] for _ in range(len(info))]

    # 트리 구성하기
    for parent, child in edges:
        tree[parent].append(child)

    def dfs(sheep, wolf, current, candidates):
        # 현재 노드 반영
        if info[current] == 0:
            sheep += 1
        else:
            wolf += 1

        # 조건 탈락
        if wolf >= sheep:
            return sheep

        # 다음 후보 노드 구성
        next_candidates = candidates.copy()
        next_candidates.remove(current)
        # 리스트 안의 리스트 방지
        next_candidates.extend(tree[current])

        # 현재 상태에서의 최대 양
        max_sheep = sheep

        # 후보 노드들로 분기
        for next_node in next_candidates:
            max_sheep = max(max_sheep, dfs(sheep, wolf, next_node, next_candidates))

        return max_sheep

    answer = dfs(0, 0, 0, [0])
    return answer
