#include <iostream>
#include <vector>
#include <stack>
#include <string>
#define MAX 101
using namespace std;

char zone[MAX][MAX];
char visited[MAX][MAX];
vector<pair<int, int>> p; // 구역 위치
stack<pair<int, int>> s; // DFS 탐색을 위한 stack
int dx[] = { 1, 0, -1, 0 }; // 상하좌우 이동을 위한 배열
int dy[] = { 0, 1, 0, -1 };

void dfs(int x, int y, int N, char color) {
    s.push({ x, y });
    visited[x][y] = 'O';

    while (!s.empty()) {
        int X = s.top().first;
        int Y = s.top().second;
        s.pop();

        for (int i = 0; i < 4; i++) {
            int nx = X + dx[i];
            int ny = Y + dy[i];

            if (nx >= 0 && ny >= 0 && nx < N && ny < N) {
                if (visited[nx][ny] == 'X' && zone[nx][ny] == color) {
                    s.push({ nx, ny });
                    visited[nx][ny] = 'O';
                }
            }
        }
    }
}

int main() {
    int N;
    int R_cnt = 0, G_cnt = 0, B_cnt = 0; // 구역 수 카운트

    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> zone[i][j];
            visited[i][j] = 'X';
            p.push_back(make_pair(i, j));
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (visited[i][j] == 'X') {
                dfs(i, j, N, zone[i][j]);

                // 색에 따른 구역 수를 카운트
                if (zone[i][j] == 'R') R_cnt++;
                else if (zone[i][j] == 'G') G_cnt++;
                else if (zone[i][j] == 'B') B_cnt++;
            }
        }
    }

    cout << R_cnt + G_cnt + B_cnt << " " <<
}
