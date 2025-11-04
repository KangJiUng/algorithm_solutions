동물 = ['척추동물', '어류', '척추동물', '무척추동물', '파충류', '척추동물', '어류', '파충류']

def solution(동물, 좌석수):
  자리 = []
  answer = 0
  for i in 동물:
    if len(자리) < 좌석수:
      if i in 자리:
        히트된자리 = 자리.pop(자리.index(i))
        자리.append(히트된자리)
        answer += 1
      else:
        자리.append(i)
        answer += 60
    else:
      if i in 자리:
        자리.append(자리.pop(0))
        answer += 1
      else:
        자리.pop(0)
        자리.append(i)
        answer += 60

  return f'{answer // 60}분 {answer % 60}초'

solution(동물, 3)
