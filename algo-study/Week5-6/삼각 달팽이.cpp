// 월간 코드 챌린지 시즌 1: 삼각 달팽이

#include <string>
#include <vector>
#include<iostream>
#include<cstring>
using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    int snail[n][n];
    int sum = 0;
    memset(snail, 0, sizeof(snail));

    for (int i = 1; i <= n; i++) { // 달팽이에 채워넣어야하는 숫자
        sum += i;
    }

    int count = 0;
    int X = -1;
    int Y = 0;

    while (count != sum) {  // 모든 숫자를 모두 채워넣을 때까지
        for (int i = 0; i < n; i++) { // 아래로 이동하며 채워넣음
            X += 1; // 행인덱스 +1
            if (snail[X][Y] == 0) { // 숫자가 없다면(배열이 비워져있다면)
                snail[X][Y] = count + 1;
                count += 1;
            }
            else { // 이미 숫자가 있다면 전 칸으로 이동 후 꺾음(삼각형의 꼭짓점)
                X -= 1;
                break;
            }
        }

        for (int i = 0; i < n - 1; i++) { // 오른쪽으로 이동하며 채워 넣음
            if (count == sum) { 
                break;
            }

            Y += 1; // 열인덱스 +1
            if (snail[X][Y] == 0) {
                snail[X][Y] = count + 1;
                count += 1;
            }
            else {
                Y -= 1;
                break;
            }
        }

        for (int i = 0; i < n - 2; i++) { // 대각선 위로 이동하며 채워넣음
            X -= 1;
            Y -= 1;
            if (snail[X][Y] == 0) {
                snail[X][Y] = count + 1;
                count += 1;

            }
            else {
                X += 1;
                Y += 1;
                break;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n && snail[i][j] != 0; j++) { // 범위 안에 있는 숫자들을 순서대로 벡터에 저장
            answer.push_back(snail[i][j]);
        }
    }

    return answer;
}