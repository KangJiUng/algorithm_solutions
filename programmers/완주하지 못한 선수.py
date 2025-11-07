# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant
# 완주한 선수들의 이름이 담긴 배열 completion
# 완주하지 못한 선수의 이름을 return

# 풀이 1 - 시간초과(O(n²))
"""
def solution(participant, completion):
    answer = ''

    for i in participant:
        if participant.count(i) > 1 and participant.count(i) > completion.count(i):
            answer = i
        else:
            if i not in completion:
                answer = i

    return answer
"""


# 풀이 2 - 시간 초과(거의 O(n³))
"""
def solution(participant, completion):
    answer = ''

    while len(participant) > 1:
        for i in completion:
            participant.remove(i)

    answer = participant[0]

    return answer
"""


# 풀이 3 - 시간 통과, 딕셔너리(해시) 이용
def solution(participant, completion):
    completion_dict = {}

    # 완주자 명단에 있는 선수 세기
    for i in completion:
        if i in completion_dict:
            completion_dict[i] += 1
        else:
            completion_dict[i] = 1

    # 참가자 명단 순회
    for i in participant:
        # 이름이 아예 없거나 이미 0으로 완주자를 셌는데 또 있으면 미완주자
        if i not in completion_dict or completion_dict[i] == 0:
            return i
        else:
            completion_dict[i] -= 1
