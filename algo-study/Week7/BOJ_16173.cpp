// 백준 16173번 점프왕 쩰리

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int N;
	cin >> N;

	vector<vector<int>> game_map(N, vector<int>(N)); // 2차원 벡터 초기화 방법 유의
	queue<pair<int, int>> q;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> game_map[i][j];
		}
	}

	q.push(make_pair(0, 0)); // 큐에 시작점 추가

	while (!q.empty()) { // 큐가 빌 때까지 반복
		int x = q.front().first; // X 좌표 설정
		int y = q.front().second; // Y 좌표 설정
		int step = game_map[x][y]; // 칸의 숫자
		q.pop(); // 현재 위치 pop

		if (step == -1) { // 현재 있는 위치가 -1이면 도달 가능
			cout << "HaruHaru";
			return 0;
		}
		if (step == 0) { // 현재 있는 위치가 0이면 더이상 이동할 수 없으므로 제외
			continue;
		}

		if (x + step < N) { // 오른쪽 방향
			q.push(make_pair(x + step, y));
		}
		if (y + step < N) { // 왼쪽 방향
			q.push(make_pair(x, y + step));
		}
	}

	cout << "Hing"; // 큐가 다 비워졌음에도 -1에 도달 불가능
	return 0;
}