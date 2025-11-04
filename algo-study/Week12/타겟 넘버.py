def solution(numbers, target):
    global answer # dfs 함수 안이랑 바깥 둘다에서 사용하기 위해 전역변수 사용
    answer = 0
    
    def dfs(cnt, sum) : # cnt는 현재까지 본 숫자의 개수
        global answer
        if cnt == len(numbers) : # 길이랑 같으면 다 확인한 것
            if sum == target :
                answer += 1
            return
            
        # 더하거나 빼는 경우를 호출
        dfs(cnt + 1, sum + numbers[cnt])
        dfs(cnt + 1, sum - numbers[cnt])
        
    dfs(0, 0)
    
    return answer
