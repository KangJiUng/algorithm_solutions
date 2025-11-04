// 백준 1388번: 바닥 장식

#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N, M;
	int cnt = 0;

	cin >> N >> M;

	vector<vector<char>> floor(N, vector<char>(M));

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> floor[i][j];
		}
	}

	for (int i = 0; i < N; i++) { // '-'는 같은 행에서 탐색하므로
		char previous = '.'; // 행이 바뀌면서 or 다른 문자로 바뀌는 시점 확인을 위한 변수
		for (int j = 0; j < M; j++) {
			if (floor[i][j] == '-') {
				if (floor[i][j] != previous) { // 장식 모양 바뀜
					cnt++;
				}
			}
			previous = floor[i][j]; // 방문했음을 표시
		}
	}

	for (int j = 0; j < M; j++) { // '|'는 같은 열에서 탐색하므로
		char previous = '.';
		for (int i = 0; i < N; i++) {
			if (floor[i][j] == '|') {
				if (floor[i][j] != previous) {
					cnt++;
				}
			}
			previous = floor[i][j];
		}
	}

	cout << cnt;
	return 0;
}