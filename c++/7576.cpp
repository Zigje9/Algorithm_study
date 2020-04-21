#include <iostream>
#include <queue>

using namespace std;
int M,N;
int tomato[1001][1001];
bool visit[1001][1001];
int move_x[4]={0,-1,0,1};
int move_y[4]={1,0,-1,0};
queue<pair<int, int>> q;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M >> N;
    for(int i=1 ; i<=N ; i++){
        for(int j=1 ; j<=M ; j++){
            cin >> tomato[i][j];
            if(tomato[i][j]==1){
                q.push({i,j});
                visit[i][j]=1;
            }
        }
    }

    while(!q.empty()){
        int now_x=q.front().first;
        int now_y=q.front().second;
        q.pop();
        for(int i=0 ; i<4 ; i++){
            int next_x=now_x+move_x[i];
            int next_y=now_y+move_y[i];
            if(next_x>0 && next_y>0 && next_x<=N && next_y<=M){
                if(visit[next_x][next_y]==0 && tomato[next_x][next_y]==0){
                    q.push({next_x,next_y});
                    tomato[next_x][next_y] = tomato[now_x][now_y]+1;
                    visit[next_x][next_y]=1;
                }
            }
        }
    }
    int answer=0;
    bool fail=false;
    int cnt=0;
    for(int i=1 ; i<=N ; i++){
        for(int j=1 ; j<=M ; j++){
            if(answer<tomato[i][j]){
                answer = tomato[i][j];
            }
            if(tomato[i][j]==0){
                fail=true;
            }
            if(tomato[i][j]==-1){
                cnt+=1;
            }
        }
    }
    if(cnt==N*M){
        cout << 0 << "\n";
        return 0;
    }
    if(fail){
        cout << -1 << "\n";
        return 0;
    }
    cout << answer-1 << "\n";

    return 0;
}
