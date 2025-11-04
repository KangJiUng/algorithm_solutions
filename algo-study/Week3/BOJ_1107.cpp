// 백준 1107번 리모컨

#include <iostream>
#include <algorithm>
using namespace std;

bool check[10]; //고장난 버튼 확인 배열

int check_broken(int n) { //고장난 숫자가 있으면 채널 pass
	int len = 0;
	if (n == 0) {
		if (check[0]) return 0;
		else return 1; //자릿수 1 반환
	}
	while (n > 0) {
		if (check[n % 10]) return 0;
		n /= 10;
		len++;
	}
	return len;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N, M;

	cin >> N >> M;

	int result = abs(N - 100); //+, - 버튼으로 이동하는 횟수를 초기값으로 설정

	for (int i = 0; i < M; i++) {
		int button_num;
		cin >> button_num;
		check[button_num] = true; //고장난 숫자 버튼을 true로 설정
	}

	if (N == 100) { //N이 100이면 현재 채널이므로 이동할 필요 X
		cout << "0";
		return 0;
	}

	for (int i = 0; i <= 9999999; i++) { //임의로
		int len = check_broken(i); //고장난 숫자가 없으면 채널의 자리수 길이 반환

		if (len) {
			result = min(result, len + abs(N - i));
		}
	}
	cout << result;
}