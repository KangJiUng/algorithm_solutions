#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, vector<int> tangerine) {
    int answer = 0;
    vector<int> count(10000001, 0);
    
    for(int i = 0; i < tangerine.size() ; i++) {
        count[tangerine[i]] ++;
    }
    
    sort(count.rbegin(), count.rend());
    
    for(int i = 0; i < count.size(); i++){
        k -= count[i];
        answer++;
        if(k <= 0) {
            return answer;
        }
    }
    
}
