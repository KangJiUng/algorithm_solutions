#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<int> order) {
    int answer = 0;
    stack<int> assistant;
    
    for(int i = 1; i <= order.size(); i++) 
    {
        assistant.push(i); // 첫 번째 상자부터 영재에게 들어옴
        while(!assistant.empty() && order[answer] == assistant.top()) // 영재에게 들어오는 상자가 order 상자랑 같은지 확인하고 같으면 트럭에 싣음
        {
            assistant.pop();
            answer++;
        }
    }
    
    return answer;
}
