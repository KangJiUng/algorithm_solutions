// 백준 1002번: 터렛

#include <iostream>
#include <cmath>
using namespace std;

double distance(double x1, double y1, double x2, double y2) { //두 점 사이의 거리 공식
	return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}

int main() {
	int T;
	int x1, y1, r1, x2, y2, r2;

	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;

		double d = distance(x1, y1, x2, y2); //두 원의 중심 사이의 거리

		if (x1 == x2 && y1 == y2) { //(x1, y1)과 (x2, y2)의 좌표가 동일할 경우
			if (r1 == r2) { //반지름이 같은 경우
				cout << "-1" << endl; //좌표의 수가 무수히 많음
			}
			else if(r1 != r2) { //반지름이 다른 경우
				cout << "0" << endl; //좌표의 수는 0개
			}
		}
		else { //(x1, y1)과 (x2, y2)의 좌표가 다를 경우
			if (r1 + r2 < d || abs(r1 - r2) > d) { //원이 떨어져 있거나 하나를 포함하는 경우
				cout << "0" << endl; //좌표의 수는 0개
			}
			else if (r1 + r2 == d || abs(r1 - r2) == d) { //원이 서로 외접하거나 내접하는 경우
				cout << "1" << endl; //좌표의 수는 1개
			}
			else if (abs(r1 - r2) < d && abs(r1 + r2) > d) { //원이 두 점에서 만나는 경우
				cout << "2" << endl; //좌표의 수는 2개
			}
		}
	}
}