//백준 11725번 트리의 부모 찾기

#include <iostream>
#include <vector>
#define MAX 100001
using namespace std;

int node[MAX]; //각 노드에 대한 부모 노드를 저장하는 배열
bool visited[MAX] = { false }; //각 노드를 방문했음을 표시하는 배열
vector<int> v[MAX]; //무방향 트리(노드 연결만)를 저장하는 벡터

void dfs(int k) {
    visited[k] = true; //방문했음을 표시
    for (int i = 0; i < v[k].size(); i++) {
        int parent = v[k][i]; 
        if (!visited[parent]) { //방문하지 않은 노드라면
            node[parent] = k; //현재 노드에 연결된 노드를 부모 노드로 우선 설정
            dfs(parent); //재귀호출
        }
    }
}

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N-1; i++) { //둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어짐
        int x, y;
        cin >> x >> y;
        v[x].push_back(y);
        v[y].push_back(x);
    }

    dfs(1);

    for (int i = 2; i <= N; i++) {
        cout << node[i] << "\n";
    }
}
