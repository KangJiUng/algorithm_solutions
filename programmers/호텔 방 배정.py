# 풀이 1 - 효율성 테스트 실패
def empty_room(room_status, number):
    while 1:
        if room_status[number] == False:
            return number
        elif room_status[number] == True:
            number += 1


def solution(k, room_number):
    answer = []
    room_status = [False for _ in range(k)]  # 0 ~ 9번

    for i in room_number:
        # 방이 비어있음
        if room_status[i - 1] == False:
            room_status[i - 1] = True
            answer.append(i)

        # 방이 이미 배정되어 있음
        elif room_status[i - 1] == True:
            empty_room_number = empty_room(room_status, i)
            room_status[empty_room_number] = True
            empty_room_number += 1
            answer.append(empty_room_number)

    return answer


# 풀이 2
def empty_room(room_status, number):
    # 해당 방이 아직 배정 안 됐으면 바로 사용
    if number not in room_status:
        room_status[number] = number + 1
        return number

    # 이미 배정된 방이면, 다음 후보로 점프
    room_status[number] = empty_room(room_status, room_status[number])
    return room_status[number]


def solution(k, room_number):
    answer = []
    room_status = {}

    for i in room_number:
        assigned_room = empty_room(room_status, i)
        answer.append(assigned_room)

    return answer
