def solution(n, words):
    answer = []
    is_used = dict()
    num = 1
    people = {i: 0 for i in range(1, n + 1)}

    for i in range(len(words)):
        if num == n + 1:
            num = 1

        if words[i] not in is_used:
            if i > 0 and words[i][0] != words[i - 1][-1]:
                people[num] += 1
                answer = [num, people[num]]
                break

            is_used[words[i]] = 0
            people[num] += 1
            num += 1
        else:
            people[num] += 1
            answer = [num, people[num]]
            break

        answer = [0, 0]

    return answer
