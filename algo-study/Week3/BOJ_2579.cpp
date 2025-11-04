// 백준 2579번 계단 오르기

#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 301
using namespace std;

int main() {
	int stair, score;
	vector<int> v; //각 계단에 대한 점수를 저장하는 벡터
	int ms[MAX]; //오르는 계단에 대한 최댓값을 저장하는 배열

	cin >> stair;

	for (int i = 0; i < stair; i++) {
		cin >> score;
		v.push_back(score);
	}

	ms[0] = v[0]; //제일 첫 번째 계단의 점수를 저장
	ms[1] = max(v[1], v[0] + v[1]); //2칸을 가는 게 최댓값인지 1칸씩 2계단을 가는 게 최댓값인지 확인하고 저장
	ms[2] = max(v[0] + v[2], v[1] + v[2]); //1->2->3계단 이동이 불가하므로 추가로 확인

	for (int i = 3; i < stair; i++) {
		ms[i] = max(
			v[i] + ms[i - 2],         //현재 계단을 오르면서 이전 계단에서 2칸 오르는 경우(예를 들어, i가 4라면 2에서 올라온 경우)
			v[i] + v[i - 1] + ms[i - 3] //현재 계단을 오르면서 이전 계단에서 1칸 오르는 경우(예를 들어, i가 4이고 3에서 올라왔다면 그 전에는 무조건 1에서 올라왔어야함)
		);
		//ms[3] = max(v[3] + ms[1], v[3] + v[2] + ms[0]) -> 두 번째 계단에서 2칸 이동 / 첫 번째 계단에서 2칸+1칸 이동 비교
		//ms[4] = max(v[4] + ms[2], v[4] + v[3] + ms[1]) -> 세 번째 계단에서 2칸 이동 / 두 번째 계단에서 2칸+1칸 이동 비교
		//                                                  4                       3
		//                                                  5                       4
		//                                                  6                       5
		//                                                  7                       6

	}

	cout << ms[stair - 1];
}