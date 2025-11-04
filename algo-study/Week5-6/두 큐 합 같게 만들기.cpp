// 2022 KAKAO TECH INTERNSHIP 두 큐 합 같게 만들기

#include <string>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> queue1, vector<int> queue2) {
    queue<int> q1, q2;
    long long sum1 = 0, sum2 = 0;

    for (auto x : queue1) { // 반복자 대신 auto를 사용해 총합 계산
        sum1 += x;
        q1.push(x);
    }

    for (auto x : queue2) {
        sum2 += x;
        q2.push(x);
    }

    // 최소 횟수 -> 큐의 길이만큼 한 번 더 도는 것이 최악의 경우 x 2 (큐가 2개)
    int N = 4 * queue1.size() + 1; 
     
    for (int i = 0; i < N; i++) {
        if (sum1 == sum2) { // 두 큐의 원소 총합이 같으면
            return i; // 횟수 그대로 반환
        }
        // 총합이 큰 쪽의 원소를 작은 쪽의 큐로 넘기고 원래 큐에서는 pop
        if (sum1 < sum2) {
            int x = q2.front();
            sum1 += x; 
            sum2 -= x;
            q1.push(x);
            q2.pop();
        } 
        else { 
            int x = q1.front();
            sum2 += x;
            sum1 -= x;
            q2.push(x);
            q1.pop();
        }
    }
    return -1; // 반복문을 다 돌아도 총합이 같지 않으면 -1 반환
}