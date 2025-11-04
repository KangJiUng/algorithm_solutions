// 백준 18310번: 안테나

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	long long N, M;
	long long distance = 0, sum = 0, min = 0;
	vector<long long> locate;

	cin >> N;

	vector<long long> house;

	for (int i = 0; i < N; i++) {
		cin >> M;
		house.push_back(M);
		min += M;
	}

	sort(house.begin(), house.end());

	int answer = house[(N - 1) / 2];

	cout << answer;


	/*
	// O(n^2)이어서 시간초과

	for (int i = N-1; i >= 0; i--) {
		sum = 0;
		for (int j = 0; j <= i; j++) {
			distance = abs(house[i] - house[j]);
			sum += distance;
		}
		if (sum < min) {
			locate.clear();
			locate.push_back(house[i]);
		}
		else if (sum == min) {
			locate.push_back(house[i]);

			sort(locate.begin(), locate.end());
		}
	}

	cout << locate[0];
	*/

	return 0;
}