from collections import Counter

def solution(topping):
    result = 0
    
    cheolsu = Counter(topping)
    brother = {} # 토핑 종류에 대한 개수를 셀 것이므로 딕셔너리 사용
    
    # 동생한테 하나씩 토핑을 나눠줌
    for i in range(len(topping)):
        if topping[i] in brother: # 동생이 이미 가지고 있는 토핑이면
            brother[topping[i]] += 1 # 토핑의 개수 +1
        else: # 없는 토핑이면
            brother[topping[i]] = 1
            
        cheolsu[topping[i]] -= 1 
        
        # 철수 해당 토핑이 없으면 철수가 가진 토핑 가짓수에서 토핑 제거
        if not cheolsu[topping[i]]:
            del(cheolsu[topping[i]])
        
        # 철수가 가진 토핑 갯수 == 동생이 가진 토핑 갯수가 같으면 1 더함
        if len(cheolsu) == len(brother):
            result += 1
            
    return result
