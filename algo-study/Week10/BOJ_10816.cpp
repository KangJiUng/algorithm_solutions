// 백준 10816번: 숫자 카드2
#include <iostream>
#include <map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    long long N, M, n;
    map<long long, long long> cards;

    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> n;
        cards[n]++; // 해당 숫자를 인덱스로 쓰고 value값 ++
    }

    cin >> M;

    for (int i = 0; i < M; i++) {
        cin >> n;
        cout << cards[n] << ' '; // 그대로 value 값 출력
    }

    return 0;
}

/* lowerbound upperbound 사용
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    long long N, M, n;
    long long cards[500002];

    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> n;
        cards[i] = n;
    }

    sort(cards, cards + N);

    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> n;
        cout << upper_bound(cards, cards + N, n) - lower_bound(cards, cards + N, n) << ' ';
    }
}
*/