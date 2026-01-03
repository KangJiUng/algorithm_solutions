def dfs(route, tickets, is_used):
    # 모든 티켓을 사용했으면 경로 완성
    if len(route) == len(tickets) + 1:
        return route

    current = route[-1]

    for i in range(len(tickets)):
        if is_used[i] == 0 and tickets[i][0] == current:
            is_used[i] = 1
            route.append(tickets[i][1])

            result = dfs(route, tickets, is_used)
            if result:
                return result  # 성공 경로 즉시 반환

            # 실패 -> 백트래킹
            is_used[i] = 0
            route.pop()

    return None  # 이 경로로는 실패


def solution(tickets):
    # 사전순 정렬
    tickets.sort(key=lambda x: (x[0], x[1]))

    is_used = [0] * len(tickets)
    route = ["ICN"]

    return dfs(route, tickets, is_used)
