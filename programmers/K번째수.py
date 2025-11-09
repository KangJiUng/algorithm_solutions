def solution(array, commands):
    answer = []

    for i in commands:
        cut_array = []
        for j in range(i[0] - 1, i[1]):
            k = i[2] - 1
            cut_array.append(array[j])

        cut_array.sort()
        answer.append(cut_array[k])

    return answer
