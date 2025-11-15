def solution(record):
    answer = []
    matching = {}
    records = []

    for i in record:
        if i[0:5] == "Enter":
            user_id = i.split(" ")[1]
            nickname = i.split(" ")[2]
            matching[user_id] = nickname
            records.append(f"Enter {user_id}")

        if i[0:5] == "Leave":
            user_id = i.split(" ")[1]
            records.append(f"Leave {user_id}")

        if i[0:6] == "Change":
            user_id = i.split(" ")[1]
            nickname = i.split(" ")[2]
            matching[user_id] = nickname

    for i in records:
        if i[0:5] == "Enter":
            user_id = i.split(" ")[1]
            nickname = matching[user_id]
            answer.append(f"{nickname}님이 들어왔습니다.")

        if i[0:5] == "Leave":
            user_id = i.split(" ")[1]
            nickname = matching[user_id]
            answer.append(f"{nickname}님이 나갔습니다.")

    return answer
