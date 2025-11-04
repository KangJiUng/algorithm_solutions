//백준 7576번 토마토

#include <iostream>
#include <queue>
#define MAX 1001
using namespace std;

//스택오버플로우 발생으로 전역변수 사용(또는 동적할당을 사용해준다.)
int N, M;
int days = 0;
int tomato[MAX][MAX];
int visited[MAX][MAX]; //방문 여부 및 소요 일수를 기록하는 배열
int dx[] = { 1, 0, -1, 0 }; //상하좌우 이동을 위한 배열
int dy[] = { 0, 1, 0, -1 };
bool check = false; //토마토가 모두 익었는지 확인하는 bool 변수
queue<pair<int, int>> q;

int main() {
	cin >> M >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> tomato[i][j];
			visited[i][j] = -1; //방문 여부 초기화

			if (tomato[i][j] == 1) { //익어있는 토마토가 있는 경우
				q.push({ i, j }); //queue에 push
				visited[i][j]++; //방문했음을 표시
			}
		}
	}

	while (!q.empty()) { //queue가 빌 때까지(익은 토마토가 없을 때까지)
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) { //상하좌우의 토마토 상태 확인
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx >= 0 && ny >= 0 && N > nx && M > ny) { //범위 내에서
				if (visited[nx][ny] == -1 && tomato[nx][ny] == 0) { //방문하지 않았고 익지 않은 토마토인 경우
					q.push({ nx, ny }); //다음 날에 익을 토마토이므로 q에 push
					visited[nx][ny] = visited[x][y] + 1; //소요 일수 +1
				}
			}
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (days < visited[i][j]) { //0보다 오래 걸린 날이 있는 경우
				days = visited[i][j]; //days에 저장(최대 일수)
			}
			if (tomato[i][j] == 0 && visited[i][j] == -1) { //익지 않은 토마토가 있고, 그 토마토를 방문하지 않은 경우
				days = -1;
				check = true; //토마토가 모두 익지 않음
				break;
			}
		}
		if (check) break;
	}
	cout << days;
}
