# 검색 및 AI 도움
# 다익스트라


def solution(n, s, a, b, fares):
    # 그래프 구성
    graph = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    # 방문하지 않은 노드 중 최소 거리 노드 찾기
    def get_min_node(dist, visited):
        min_node = -1
        min_dist = float("inf")

        for i in range(1, n + 1):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_node = i

        return min_node

    def dijkstra(start):
        dist = [float("inf")] * (n + 1)
        visited = [False] * (n + 1)
        dist[start] = 0

        for _ in range(n):
            cur = get_min_node(dist, visited)
            if cur == -1:
                break

            visited[cur] = True

            for nxt, cost in graph[cur]:
                if dist[nxt] > dist[cur] + cost:
                    dist[nxt] = dist[cur] + cost

        return dist

    # 다익스트라 3번
    dist_s = dijkstra(s)
    dist_a = dijkstra(a)
    dist_b = dijkstra(b)

    # 합승 분기점 계산
    # 모든 합승 분기점 k에 대해 (s -> k) + (k -> a) + (k -> b) 비용을 계산하기 위해
    # s, a, b를 시작점으로 다익스트라를 각각 한 번씩만 수행한다.
    answer = float("inf")
    for k in range(1, n + 1):
        cost = dist_s[k] + dist_a[k] + dist_b[k]
        if cost < answer:
            answer = cost

    return answer
