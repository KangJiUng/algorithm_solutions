//백준 1654번 랜선 자르기

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int K, N;
    int length;
    vector<int> cables; // 랜선의 길이를 저장할 벡터

    cin >> K >> N;

    for (int i = 0; i < K; ++i) {
        cin >> length;
        cables.push_back(length);
    }

    sort(cables.rbegin(), cables.rend()); // 랜선의 길이 내림차순 정렬

    int low = 1;
    int high = cables[0]; // 이분 탐색을 위한 시작과 끝 값(내림차순 정렬했으므로 index 0) 설정

    while (low <= high) {
        int mid = (low + high) / 2;
        int count = 0;

        for (int i = 0; i < K; ++i) { // 현재 길이로 만들 수 있는 랜선의 개수 계산
            count += (cables[i] / mid);
        }

        if (count >= N) {  // N개 이상의 랜선을 만들 수 있는 경우(mid 값 아래로는 어차피 N개 이상이 가능함)
            low = mid + 1;
        }
        else { // N개를 만들 수 없는 경우
            high = mid - 1;
        }
    }

    // 최대 랜선의 길이 출력
    cout << low - 1; //또는 high...
}
