// 백준 17413번 단어 뒤집기 2

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	string S;
	vector<char> v;

	getline(cin, S);

	for (int i = 0; i < S.length(); i++) {
		if (S[i] == '<') { // '<'를 만나면
			while (S[i] != '>') { // '>'가 나올 때까지 벡터에 저장
				v.push_back(S[i]);
				i++;
			}
			v.push_back(S[i]); // '>'도 추가
			for (int j = 0; j < v.size(); j++) { //그대로 출력(태그)
				cout << v[j];
			}
			v.clear(); //중복 출력을 막기위해 벡터를 비워줌
		}
		else { //태그가 아니라 단어 or 숫자면
			v.push_back(S[i]); //벡터에 우선 저장
			if (S[i] == ' ' || S[i] == '<' || S[i] == '\n') { //공백 or '<' or 개행문자를 만나면
				reverse(v.begin(), v.end()); //벡터 속의 단어(숫자)를 뒤집고
				for (int j = 1; j < v.size(); j++) { //뒤집은 단어(숫자)를 출력
					cout << v[j];
				}
				cout << " ";
				v.clear();
			}
		}
	}
}
