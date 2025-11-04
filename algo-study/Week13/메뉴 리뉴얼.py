from itertools import combinations

def solution(orders, course):
    answer = []
    
    for i in course: # 스카피가 만들려는 코스요리의 메뉴 개수
        comb_counts = {} # 가능한 코스요리와 그 개수를 저장할 딕셔너리
        
        for j in orders: # 손님이 주문한 각 단품메뉴들 확인
            for comb in combinations(sorted(j), i): # 정렬된 한 주문의 단품메뉴들에서 가능한 조합들 확인
                if comb in comb_counts: # 조합이 이미 가능한 코스요리로 저장이 되었다면
                    comb_counts[comb] += 1
                else:
                    comb_counts[comb] = 1
        
        if comb_counts: # 하나의 조합이라도 나왔다면
            max_count = max(comb_counts.values()) # 가장 많이 주문된 조합의 개수를 확인
            if max_count > 1: # 최소 2번 이상 주문됐다면
                for combo, count in comb_counts.items():
                    if count == max_count: # 현재 조합의 주문횟수가 최대라면
                        answer.append(''.join(combo)) # 각 코스요리의 메뉴를 문자열로 변환하고 answer에 추가
    
    answer.sort()
    return answer
