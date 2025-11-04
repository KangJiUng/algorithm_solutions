//백준 1158번 요세푸스 문제

#include <iostream>
#include <list>
using namespace std;

int main(void) {
    int N, K;
    list<int> L;

    cin >> N >> K;

    if (N == 1) { // N이 1이면 그냥 <1>을 출력하고 끝냄
        cout << "<1>";
        return 0;
    }
    else {
        for (int i = 1; i <= N; i++) { // 1~N 까지의 숫자 리스트에 추가
            L.push_back(i);
        }

        list<int>::iterator iter = L.begin();

        cout << "<";

        while (L.size()) {
            for (int i = 1; i < K; i++) { // 1번째 사람부터 K-1번째 사람까지
                if (++iter == L.end()) { // 다음 반복자가 리스트의 끝이면
                    iter = L.begin(); // 반복자를 다시 처음으로
                    continue;
                }
            }

            if (L.size() == 1) {
                cout << *iter;  // 반복자는 * 연산자를 사용하여 컨테이너 내부의 원소를 가리키고 접근할 수 있어야함
            }
            else {
                cout << *iter << ", ";
            }

            iter = L.erase(iter);

            iter = (iter == L.end()) ? L.begin() : iter; // 삭제한 원소 자리가 이미 end인 경우 begin으로 보냄
        }

        cout << ">";
    }
}
