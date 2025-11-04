// 백준 1932번: 정수 삼각형

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    int max_sum = 0;
    int triangle[501][501];

    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cin >> triangle[i][j];
        }
    }

    for (int i = 0; i < n; i++) { // 범위 설정 주의...
        for (int j = 0; j <= i; j++) {
            if (j == 0) { // 첫째 열(젤 왼쪽)은 대각선 위가 무조건 선택됨
                triangle[i][j] += triangle[i - 1][0];
            }
            else if (i == j) { // 행과 열의 인덱스 숫자가 같은 경우(젤 오른쪽)는 대각선 위가 무조건 선택됨
                triangle[i][j] += triangle[i - 1][j - 1];
            }
            else { // 대각선 위 양쪽 둘 중 하나 선택
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j]);
            }
            max_sum = max(max_sum, triangle[i][j]); // 최댓값 갱신
        }
    }

    cout << max_sum << '\n';

    return 0;
}



