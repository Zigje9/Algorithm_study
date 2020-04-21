#include <iostream>
#include <queue>
#include <string.h>

using namespace std;
int w,h,cnt;
bool map[51][51];
bool island[51][51];
int move_x[8] = {1,1,0,-1,-1,-1,0,1};
int move_y[8] = {0,-1,-1,-1,0,1,1,1};
queue<pair<int,int>> q;

void bfs(int x,int y){
    island[x][y]=1;
    q.push({x,y});
    while(!q.empty()){
        int now_x = q.front().first;
        int now_y = q.front().second;
        q.pop();
        for(int i=0 ; i<8 ; i++){
            int next_x = now_x + move_x[i];
            int next_y = now_y + move_y[i];
            if(next_x>0 && next_y>0 && next_x<=h && next_y<=w){
                if(map[next_x][next_y]==1 && island[next_x][next_y]==0){
                    q.push({next_x,next_y});
                    island[next_x][next_y]=1;
                }
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    while(1){
        cin >> w >> h;
        if(w==0 || h==0){
            break;
        }
        for(int i=1 ; i<=h ; i++){
            for(int j=1 ; j<=w ; j++){
                cin >> map[i][j];
            }
        }
        cnt = 0;
        for(int i=1 ; i<=h ; i++){
            for(int j=1 ; j<=w ; j++){
                if(map[i][j]==1 && island[i][j]==0){
                    bfs(i,j);
                    cnt++;
                }
            }
        }
        
        cout << cnt << "\n";

        memset(map,false,sizeof(map));
        memset(island,false,sizeof(island));
    }

    return 0;
}