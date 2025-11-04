// 백준 14501번: 퇴사

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, T, P;
    int max = 0;

    cin >> N;

    vector<pair<int, int>> counsell(N + 1);

    for (int i = 1; i <= N; i++) {
        cin >> T >> P;
        counsell[i] = make_pair(T, P);
    }

    for (int i = 1; i <= N; i++) {
        int sum = 0;

        while (i <= N) {
            if (i + counsell[i].first <= N + 1) { // 종료일이 N을 넘지 않는지 확인
                sum += counsell[i].second; // 상담 총 수익 갱신
                i += counsell[i].first; // 다음 상담 일자로 이동
            }
            else {
                break;
            }
        }

        if (sum > max) { // 최대 수익 갱신
            max = sum;
        }
    }

    cout << max;
    return 0;
}
