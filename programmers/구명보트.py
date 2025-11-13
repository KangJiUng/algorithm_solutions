# 구명보트는 작아서 한 번에 최대 2명씩
# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return


def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1

    while left <= right:
        # 가장 무거운 사람이 가장 가벼운 사람과 탈 수 있으면
        if people[left] + people[right] <= limit:
            answer += 1
            right -= 1
            left += 1
        else:
            answer += 1
            right -= 1

    return answer
