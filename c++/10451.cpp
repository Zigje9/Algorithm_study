#include <iostream>
#include <vector>
#include <queue>
#include <string.h>
 
using namespace std;
int T;
vector<int> v[1001];
queue<int> q;
bool visit[1001];

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
    cin >> T;

    while(T-->0){
        int N,a;
        int cnt=0;
        cin >> N;
        for(int i=1 ; i<=N ; i++){
            cin >> a;
            v[i].push_back(a);
        }
        for(int i=1 ; i<=N ; i++){
            if(visit[i]==false){
                bfs(i);
                cnt++;
            }
        }
        cout << cnt << "\n";
        memset(visit,false,sizeof(visit));
        for(int i=1 ; i<=N ; i++){
            v[i].clear();
        }
    }
    return 0;
}