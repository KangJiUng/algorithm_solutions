//백준 1213번 팰린드롬 만들기
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
using namespace std;

int main() {
	int cnt = 0;
	string s, front, mid, back;
	map<char, int> mp;

	cin >> s;

	for (char c : s) mp[c]++; //각 알파벳에 대한 개수(길이) 할당

	if (s.length() % 2 == 0) { //문자열의 길이가 짝수인 경우
		for (auto iter : mp) {
			if (iter.second % 2 != 0) { //알파벳의 개수가 홀수인 경우가 존재
				cout << "I'm Sorry Hansoo"; //팰린드롬 생성 불가
				exit(0); //반복문 종료
			}
		}
	}
	else { //문자열의 길이가 홀수인 경우
		for (auto iter : mp) {
			if (iter.second % 2 != 0) { //알파벳의 개수가 홀수인 경우 카운트
				mid = iter.first;
				cnt++;
			}
			if (cnt >= 2) { //홀수개인 알파벳 종류 2개 이상
				cout << "I'm Sorry Hansoo"; //팰린드롬 생성 불가
				exit(0);
			}
		}
	}

	for (auto iter : mp) { //front, back 설정
		for (int i = 0; i < iter.second / 2; i++) { //알파벳 개수의 1/2만큼 저장
			front += iter.first; //string 자료형은 + 사용 가능
			back += iter.first;
		}
	}
	reverse(back.begin(), back.end()); //팰린드롬 완성을 위해 back 문자열 reverse
	cout << front + mid + back;
}