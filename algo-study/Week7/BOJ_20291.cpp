// 백준 20291번 파일 정리

#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main() {
	int N;
	string file_name;
	map<string, int> file_extension; // 확장자-확장자 개수를 저장하기 위한 map 선언

	cin >> N;

	for (int i = 0; i < N; i++) {
		int cnt = 0;
		cin >> file_name;
		file_name.erase(0, file_name.find('.') + 1); // 처음부터 .까지 삭제

		if (file_extension.find(file_name) == file_extension.end()) { // 확장자명이 map에 없으면
			file_extension.insert(make_pair(file_name, cnt)); // map에 저장
			file_extension[file_name]++; // 저장 후 개수 +1
		}
		else {
			file_extension[file_name]++; // 확장자명이 map에 있으면, 그 확장자 개수 +1 
		}
	}
	for (const auto map : file_extension) {
		cout << map.first << " " << map.second << '\n';
	}

	return 0;
}