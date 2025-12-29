def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    pa = find(parent, a)
    pb = find(parent, b)
    if pa != pb:
        parent[pb] = pa


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]
    count = 0  # 선택한 다리 개수

    for i, j, cost in costs:
        if count == n - 1:
            break

        # 연결되어있지 않은 경우 연결
        if find(parent, i) != find(parent, j):
            union(parent, i, j)
            answer += cost
            count += 1

    return answer
