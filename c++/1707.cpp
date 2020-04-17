#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>

using namespace std;

queue<int> q;
vector<int> v[20001];
bool visit[20001];
int color[20001];
int set[20001];
int T;

void bfs(int start){
    if(visit[start]==true){
        return;
    }
    q.push(start);
    visit[start]=true;
    color[start]=1;
    while(!q.empty()){
        int num = q.front();
        q.pop();
        for(int i=0 ; i<v[num].size() ; i++){
            int next = v[num][i];
            if(!visit[next]){
                q.push(next);
                visit[next]=true;
                if(color[num]==1){
                    color[next]=2;
                }
                if(color[num]==2){
                    color[next]=1;
                }
            }
        }
    }
}

bool isBipartiteGraph(int V){
    for (int i = 1 ; i <= V ; i++) {
        int size = v[i].size();
        for (int j = 0 ; j < size ; j++) {
            int next = v[i][j];
            if (color[i] == color[next]) {
                return 0;
            }
        }
    }
    return 1;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    while(T-->0){
        int V,E,a,b;
        cin >> V >> E;
        for(int i=0 ; i<E ; i++){
            cin >> a >> b;
            v[a].push_back(b);
            v[b].push_back(a);
        }
        for(int i=1 ; i<=V ; i++){
            bfs(i);
        }
        if(isBipartiteGraph(V)==1){
            cout << "YES" << "\n";
        }
        else{
            cout << "NO" << "\n";
        }

        for(int i=1 ; i<=V ; i++){
            v[i].clear();
        }

        memset(visit, false, sizeof(visit));
        memset(color, 0, sizeof(color));
        memset(set, 0, sizeof(set));

    }
    return 0;
}
