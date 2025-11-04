// 백준 10451번: 순열 사이클

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N;
        int cnt = 0;

        cin >> N;

        vector<int> graph(N + 1);
        vector<bool> visited(N + 1, false);

        for (int i = 1; i <= N; ++i) {
            cin >> graph[i];
        }

        for (int i = 1; i <= N; ++i) { // 기준을 벡터에 저장된 숫자 하나씩 잡으면서 반복
            if (!visited[i]) {
                int node = i; // 그냥 i로 쓰면 안됨
                while (!visited[node]) { // 방문하지 않은 node면
                    visited[node] = true;  // 방문 처리
                    node = graph[node]; // 문제조건 만족시키도록 연결
                }
                cnt++; // 사이클 횟수 추가
            }
        }

        cout << cnt << '\n';
    }

    return 0;
}
