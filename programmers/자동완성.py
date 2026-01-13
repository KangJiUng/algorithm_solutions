def diff(near_word, current_word):
    cnt = 0

    for i in range(min(len(near_word), len(current_word))):
        if near_word[i] == current_word[i]:
            cnt += 1
        else:
            break

    return cnt


def solution(words):
    answer = 0
    sorted_words = sorted(words)

    for i in range(len(sorted_words)):
        current_word = sorted_words[i]

        # 앞 단어와의 공통 접두사
        if i > 0:
            front_cnt = diff(sorted_words[i - 1], current_word)
        else:
            front_cnt = 0

        # 뒤 단어와의 공통 접두사
        if i < len(sorted_words) - 1:
            back_cnt = diff(current_word, sorted_words[i + 1])
        else:
            back_cnt = 0

        # 둘 중 더 많이 겹치는 쪽 + 1
        need = max(front_cnt, back_cnt) + 1

        # 단어의 길이가 최대 길이
        answer += min(len(current_word), need)

    return answer
