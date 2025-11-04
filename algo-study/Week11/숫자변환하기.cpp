#include <string>
#include <vector>

using namespace std;

int solution(int x, int y, int n) {
    int answer = 0;
    vector<int> DP(y + 1, 1000001); // y범위에 벗어나는 값으로 초기화
    
    DP[x] = 0; // 연산횟수 계산을 위해 시작 배열 0으로 초기화
    
    for (int i = x + 1; i <= y; i++) { // 3가지의 연산에 대해 조건연산 시작
        if (i >= n && i - n >= x) { // x에 n을 더하는 연산
            DP[i] = min(DP[i], DP[i - n] + 1);
        }
        if (i / 2 >= x && i % 2 == 0) { // x에 2를 곱하는 연산
            DP[i] = min(DP[i], DP[i / 2] + 1);
        }
        if (i / 3 >= x && i % 3 == 0) { // x에 3을 곱하는 연산
            DP[i] = min(DP[i], DP[i / 3] + 1);
        }
    }

    answer = DP[y];

    if (DP[y] >= 1000001) { // y값에 연산횟수가 들어가 있지 않으면 x에서 y 도달 불가
        return -1; 
    }
    else {
        return answer;
    }
}
