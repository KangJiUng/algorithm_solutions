def solution(n, k):
    remain = ""
    
    while n:           
        remain = str(n % k) + remain
        n = n // k
        
    remain = remain.split("0")
    
    result = 0
    
    for i in remain :
        if i == "" or int(i) < 2 :
            continue
            
        prime = True
        
        for j in range(2, int(int(i)**0.5)+1) :
            if int(i) % j == 0 :
                prime = False
                break
        
        if prime :
            result += 1
            
    return result
