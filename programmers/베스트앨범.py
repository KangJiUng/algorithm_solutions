# 장르 별로 가장 많이 재생된 노래를 최대 두 개까지 모아 베스트 앨범을 출시


def solution(genres, plays):
    answer = []
    cnt_genre = {}  # 많이 재생된 장르 확인용
    cnt_plays = {}  # 장르 내에서 많이 재생된 노래 확인용

    # 해시 만들기
    for i in range(len(genres)):
        if genres[i] not in cnt_genre:
            cnt_genre[genres[i]] = plays[i]
            cnt_plays[genres[i]] = []
        else:
            cnt_genre[genres[i]] += plays[i]

    # 많이 재생된 장르 확인을 위해 내림차순 정렬
    sorted_genres = sorted(cnt_genre.items(), key=lambda x: x[1], reverse=True)

    # 해당 장르에 노래 추가
    for i in range(len(genres)):
        cnt_plays[genres[i]].append((plays[i], i))

    # 노래 많이 들은 순으로 내림차순 정렬
    # 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저
    for key in cnt_plays:
        cnt_plays[key].sort(key=lambda x: (-x[0], x[1]))

    # 베스트 앨범 수록
    for genre, _ in sorted_genres:
        answer.append(cnt_plays[genre][0][1])
        if len(cnt_plays[genre]) > 1:
            answer.append(cnt_plays[genre][1][1])

    return answer
