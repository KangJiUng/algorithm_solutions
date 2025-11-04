// 2022 KAKAO BLIND RECRUITMENT: 주차 요금 계산

#include <string>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    map<string, vector<string>> get_in; // 각 차량의 입차 시간 저장
    map<string, int> time_of_use; // 각 차량의 주차 이용 시간 저장

    for (string record : records) {
        stringstream ss(record);
        string time, carNum, info;
        ss >> time >> carNum >> info;

        // 입차 내역인 경우
        if (info == "IN") {
            get_in[carNum].push_back(time);
        }
        else {
            
        }
    }

    return answer;
}