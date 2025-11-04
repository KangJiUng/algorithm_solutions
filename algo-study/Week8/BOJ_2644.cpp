#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int n, m, mem1, mem2, parent, child;
    cin >> n;
    cin >> mem1 >> mem2;
    cin >> m;

    vector<vector<int>> relation(n + 1); // 관계 구성 2차원 벡터(한 노드에 대해 관련된 노드를 저장하기 위해 2차원)
    vector<int> distance(n + 1, 0); // 두 mem 사이의 거리 저장 벡터
    queue<int> q;

    for (int i = 0; i < m; i++) {
        cin >> parent >> child;
        relation[parent].push_back(child); // 양방향 트리 구성
        relation[child].push_back(parent);
    }

    q.push(mem1); // 찾아야 하는 둘 중 한 명 먼저 넣음

    while (!q.empty()) {
        int x = q.front();
        q.pop();

        if (x == mem2) {  // 찾아야 하는 둘 중 나머지 한 명 찾으면 끝
            cout << distance[x] << '\n';
            return 0;
        }

        for (int i = 0; i < relation[x].size(); i++) { 
            int y = relation[x][i];

            if (distance[y] == 0) { // 아직 방문하지 않은 노드라면
                q.push(y);
                distance[y] = distance[x] + 1;
            }
        }
    }
    cout << "-1" << '\n'; // 같은 트리에 없으므로 친척관계 x
    return 0;
}
