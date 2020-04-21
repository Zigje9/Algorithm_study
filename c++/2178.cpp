#include <iostream>
#include <queue>

using namespace std;
int N,M;
int map[101][101];
int miro[101][101];
bool visit[101][101];
int move_x[4]={0,1,-1,0};
int move_y[4]={1,0,0,-1};
queue<pair<int,int>> q;

void bfs(int x,int y){
    visit[x][y]=1;
    miro[x][y]=1;
    q.push({x,y});
    while(!q.empty()){
        int now_x=q.front().first;
        int now_y=q.front().second;
        q.pop();
        for(int i=0 ; i<4 ; i++){
            int next_x=now_x+move_x[i];
            int next_y=now_y+move_y[i];
            if(next_x>0 && next_x<=N && next_y>0 && next_y<=M){
                if(visit[next_x][next_y]==0 && map[next_x][next_y]==1){
                    q.push({next_x,next_y});
                    visit[next_x][next_y]=1;
                    miro[next_x][next_y]=miro[now_x][now_y]+1;
                }
            }
        }
    }
}

int main(){
    scanf("%d %d",&N,&M);
    for(int i=1 ; i<=N ; i++){
        for(int j=1 ; j<=M ; j++){
            scanf("%1d",&map[i][j]);
        }
    }
    bfs(1,1);
    printf("%d",miro[N][M]);
    return 0;
}