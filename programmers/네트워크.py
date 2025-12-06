def dfs(node, computers, visited):
    visited[node] = 1

    for next_node in range(len(computers)):
        if computers[node][next_node] == 1 and visited[next_node] == 0:
            dfs(next_node, computers, visited)


def solution(n, computers):
    visited = [0] * n
    answer = 0

    for i in range(n):
        if visited[i] == 0:
            dfs(i, computers, visited)
            answer += 1

    return answer
