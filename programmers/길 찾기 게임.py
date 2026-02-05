# 임의의 노드 V의 왼쪽 서브 트리(left subtree)에 있는 모든 노드의 x값은 V의 x값보다 작다.
# 임의의 노드 V의 오른쪽 서브 트리(right subtree)에 있는 모든 노드의 x값은 V의 x값보다 크다.
# => 서브 트리 나눠서 순회

from sys import setrecursionlimit

setrecursionlimit(10**7)  # 파이썬 재귀 limit이 1000 -> 테케 6, 7번 런타임 에러


def solution(nodeinfo):
    answer = [[]]
    # (x, y, 노드번호) 형태로 변환
    nodes = [(x, y, i + 1) for i, (x, y) in enumerate(nodeinfo)]

    # x좌표 기준 정렬 (좌 / 우 분할용)
    nodes.sort(key=lambda x: x[0])

    preorder = []
    postorder = []

    def dfs(subtree):
        if not subtree:
            return

        # y가 가장 큰 노드가 루트
        root_idx = 0
        for i in range(len(subtree)):
            if subtree[i][1] > subtree[root_idx][1]:
                root_idx = i

        # 전위 순회
        preorder.append(subtree[root_idx][2])

        # 좌 / 우 서브트리
        dfs(subtree[:root_idx])
        dfs(subtree[root_idx + 1 :])

        # 후위 순회
        postorder.append(subtree[root_idx][2])

    dfs(nodes)

    answer = [preorder, postorder]
    return answer
