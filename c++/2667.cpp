#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>

using namespace std;

int N;
int map[26][26];
int visit[26][26];

int move_X[4] = {1, 0, -1, 0};
int move_Y[4] = {0, 1, 0, -1};

queue<pair<int,int>> q;
vector<int> answer;

int bfs(int x, int y){
    int answer = 0;
    visit[x][y]=1;
    q.push({x,y});
    while(!q.empty()){
        int current_x=q.front().first;
        int current_y=q.front().second;
        answer += 1;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int next_x = current_x + move_X[i];
            int next_y = current_y + move_Y[i];
            if(next_x>0 && next_x<=N && next_y>0 && next_y<=N){
                if(map[next_x][next_y]!=0 && visit[next_x][next_y]==0){
                    q.push({next_x,next_y});
                    visit[next_x][next_y]=1;
                }
            }
        }
    }
    return answer;
}

int main(){
    cin >> N;
    for(int i=1 ; i<=N ; i++){
        for(int j=1 ; j<=N ; j++){
            scanf("%1d",&map[i][j]);
        }
    }

    for(int i=1 ; i<=N ; i++){
        for(int j=1 ; j<=N ; j++){
            if(map[i][j]==1 && visit[i][j]==0){
                answer.push_back(bfs(i,j));
            }
        }
    }

    sort(answer.begin(),answer.end());
    cout << answer.size() << "\n";
    for(int i=0 ; i<answer.size() ; i++){
        cout << answer[i] << "\n";
    }
    return 0;
}