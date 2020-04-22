#include <iostream>
#include <queue>
#include <vector>
#include <stdlib.h>

using namespace std;
int N,island;
int map[101][101];
int move_x[4]={0,1,0,-1};
int move_y[4]={1,0,-1,0};
bool visit[101][101];
queue<pair<int,int>> q;
vector<pair<pair<int,int>,int>> v;

void bfs(int x,int y,int island){
    visit[x][y]=1;
    q.push({x,y});
    map[x][y]=island;
    while(!q.empty()){
        int now_x = q.front().first;
        int now_y = q.front().second;
        q.pop();
        for(int i=0 ; i<4 ; i++){
            int next_x=now_x+move_x[i];
            int next_y=now_y+move_y[i];
            if(next_x>0 && next_x<=N && next_y>0 && next_y<=N){
                if(visit[next_x][next_y]==0 && map[next_x][next_y]!=0){
                    q.push({next_x,next_y});
                    visit[next_x][next_y]=1;
                    map[next_x][next_y]=island;
                }
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i=1 ; i<=N ; i++){
        for(int j=1 ; j<=N ; j++){
            cin >> map[i][j];
        }
    }
    island = 1;
    for(int i=1 ; i<=N ; i++){
        for(int j=1 ; j<=N ; j++){
            if(map[i][j]==1){
                island++;
                bfs(i,j,island);
            }
        }
    }

    for(int i=1 ; i<=N ; i++){
        for(int j=1 ; j<=N ; j++){
            if(map[i][j]>1){
                v.push_back({{i,j},map[i][j]});
            }
        }
    }
    int answer = 1000;

    while(v.size()>1){
        for(int i=0 ; i<v.size()-1 ; i++){
            if(v[v.size()-1].second != v[i].second){
                if(abs(v[v.size()-1].first.first-v[i].first.first)+abs(v[v.size()-1].first.second-v[i].first.second)-1<answer){
                    answer = abs(v[v.size()-1].first.first-v[i].first.first)+abs(v[v.size()-1].first.second-v[i].first.second)-1;
                }
            }
        }
        v.pop_back();
    }

    cout << answer;
    return 0;
}