// 백준 1931번 회의실 배정

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool compare(pair<int, int> &a, pair<int, int> &b) {
    if (a.second == b.second) {
        return a.first < b.first; //끝나는 시간이 같으면 시작 시간이 빠른 순으로 정렬
    }
    return a.second < b.second; //끝나는 시간이 빠른 순으로 정렬
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    int cnt = 0;
    vector<pair<int, int>> pv; //회의 시작시간, 끝나는 시간

    cin >> N;

    for (int i = 0; i < N; i++) {
        int start, end;
        cin >> start >> end;
        pv.push_back(make_pair(start, end));
    }

    sort(pv.begin(), pv.end(), compare); 

    int endtime = 0; //처음 회의는 끝나는 시간이 어떻든 우선 선택됨

    for (int i = 0; i < pv.size(); i++) {
        if (pv[i].first >= endtime) { //현재 회의의 시작시간이 이전 회의의 끝나는 시간보다 크거나 같으면
            endtime = pv[i].second; //이전 회의의 끝나는 시간을 현재로 갱신
            cnt++; //회의 추가
        }
    }

    cout << cnt << "\n";
}

