#include <string>
#include <vector>
using namespace std;

vector<int> solution(vector<int> sequence, int k) {
	vector<int> answer;

	int len = sequence.size(); // 갱신될 부분 수열의 길이
	int sum = 0, min = len; // start와 end까지의 부분 수열의 합
	pair<int, int> p = { 0, sequence.size() - 1 }; // 부분 수열의 start와 end를 저장

	for (int start = 0, end = 0; start < min;) {
		if (sum == k && len > (end - start)) { // k와 합이 같고 부분 수열의 길이가 이전보다 짧으면
			p.first = start;
			p.second = end - 1; // end는 부분 수열의 끝 자리, 즉 수열 마지막 원소의 다음 인덱스 값을 가리키기 때문
			min = (end - start);
		}
		else if (sum < k && end < min) { // k보다 합이 작으면 끝 값을 증가 시킴
			sum += sequence[end++];
		}
		else { // k보다 합이 크면 시작 값을 앞으로 당김
			sum -= sequence[start++];
		}
	}

	answer.push_back(p.first);
	answer.push_back(p.second);

	return answer;
}