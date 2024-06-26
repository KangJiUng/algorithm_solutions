## 📝1932번: 정수 삼각형
##### 알고리즘 구상
- 맨 위층부터 시작: 첫째 줄 숫자는 합에 무조건 들어감
- 둘째 줄부터는 이전에 선택된 인덱스를 기준으로 -1이나 +1의 인덱스에 위치한 숫자 중 더 큰 걸 선택(범위를 벗어나지 않는다는 가정하에)
- 선택된 수의 합을 삼각형 벡터에 저장하면서 최대를 갱신함

##### 참고 자료

##### 문제 풀이
- 맨 위층을 먼저 더해주면 점화식 헷갈림 -> 아예 점화식으로 조건문에서 사용
- 범위를 벗어나지 않는다는 가정 -> 어차피 한 숫자에는 양쪽으로 달려 있음... 할 필요x
- i=j인 곳에서는 젤 오른쪽이라 / j=0인 곳에서는 젤 왼쪽이라 무조건 대각선 위 하나만 선택
- max로 비교해서 최댓값 갱신

---

## 📝10816번: 숫자 카드 2
##### 알고리즘 구상
- 숫자 카드의 개수와 카드에 적혀있는 수의 범위가 굉장히 크기 때문에 자료형 사용과 시간 복잡도에 유의해야할 것 같음
- map만 써서도 가능할 듯? key값에 대한 value값을 입력 받으면서 바로바로 ++해줌

##### 참고 자료
- https://12bme.tistory.com/120

##### 문제 풀이
- 알고리즘 구상과 동일

---

## 📝10451번: 순열 사이클
##### 알고리즘 구상
- 벡터 1 인덱스부터 방문 안 했으면 1~N이랑 그래프의 1~N에 인덱스랑 연결시키고 연결 하나(사이클 하나)가 끝나면 다음 인덱스로 넘어가면서 사이클 개수를 셈

##### 참고 자료
- https://m.blog.naver.com/occidere/220923695595

##### 문제 풀이
- 알고리즘 구상과 동일
