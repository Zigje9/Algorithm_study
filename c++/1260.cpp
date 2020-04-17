#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
queue<int> q;
vector<int> v[1001];
bool visit_b[1001];
bool visit_d[1001];

void dfs(int start){
    if(visit_d[start]==true){
        return;
    }
    visit_d[start] = true;
    cout << start << " ";
    for(int i=0 ; i<v[start].size() ; i++){
        int next = v[start][i];
        dfs(next);
    }
}


void bfs(int start){
    q.push(start);
    visit_b[start]=true;

    while(!q.empty()){
        cout << q.front() << " ";
        int num = q.front();
        q.pop();
        for(int i=0 ; i<v[num].size() ; i++){
            int temp = v[num][i];
            if(!visit_b[temp]){
                q.push(temp);
                visit_b[temp] = true;
            }
        }
    }
}


int N,M,V;
int a,b;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M >> V;
    for(int i=0 ; i<M ; i++){
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    for(int i=1 ; i<=N ; i++){
        sort(v[i].begin(),v[i].end());
    }
    dfs(V);
    cout << "\n";
    bfs(V);

    return 0;
}