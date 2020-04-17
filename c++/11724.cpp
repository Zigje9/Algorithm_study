#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

queue<int> q;
vector<int> v[1001];
bool visit[1001];
int N,M,a,b;

void bfs(int start){
    if(visit[start]==true){
        return;
    }
    q.push(start);
    visit[start]=true;
    
    while(!q.empty()){
        int num = q.front();
        q.pop();
        for(int i=0 ; i<v[num].size() ; i++){
            int next = v[num][i];
            if(visit[next]==false){
                q.push(next);
                visit[next]=true;
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    for(int i=0 ; i<M ; i++){
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    int cnt = 0;
    for(int i=1 ; i<=N ; i++){
        if(visit[i]==false){
            bfs(i);
            cnt+=1;
        }
    }

    cout << cnt;
    return 0;
}