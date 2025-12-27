def solution(m, n, puddles):
    answer = 0
    grid = [[0] * (m + 1) for _ in range(n + 1)]
    grid[1][1] = 1

    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if [x, y] in puddles:
                continue

            grid[y][x] += grid[y - 1][x] + grid[y][x - 1]

    answer = grid[y][x] % 1000000007
    return answer
