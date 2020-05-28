#include <iostream>
#include <queue>
#include <vector>
#include <string.h>
#include <stack>

using namespace std;

int map[1001][1001];
bool visit[1001][1001];
int move_r[4] = {0, 1, 0, -1};
int move_c[4] = {1, 0, -1, 0}; //0R 1D 2L 3U
int R,C;
vector<pair<int,string>> v;
stack<pair<int,int>> s;

void dfs(int start_r, int start_c, int end_r, int end_c){
    s.push(make_pair(start_r,start_c));
    visit[start_r][start_c]=1;
    if(start_r == end_r && start_c == end_c){
        vector<pair<int,int>> out_n;
        while(!s.empty()){
            out_n.push_back(make_pair(s.top().first,s.top().second));
            s.pop();
        }
        int N = out_n.size();
        for(int i=N-1 ; i>=0 ; i--){
            cout << "(" << out_n[i].first << "," << out_n[i].second << ")" << " ";
        }
        cout << "\n";
        return;
    }
    else{
        for(int i=0 ; i<4 ; i++){
            int next_r = start_r + move_r[i];
            int next_c = start_c + move_c[i];
            if(next_r>=1 && next_c>=1 && next_r<=R && next_c<=C){ // map 범위안에 있는지 검사 
                if(visit[next_r][next_c]==0){ // 방문 검사 
                    dfs(next_r,next_c,end_r,end_c);
                    visit[next_r][next_c]=0;
                }
                else{
                    return;
                }
            }
            else{
                return;
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> R >> C;
    for(int i=1 ; i<=R ; i++){
        for(int j=1 ; j<=C ; j++){
            cin >> map[i][j];
        }
    }

    if(R%2 == 0){ // 행이 짝수인 경우 
        dfs(1,1,R,C);
    }
    else{ // 행이 홀수인 경우
        for(int i=1 ; i<C ; i++){
            cout << "R";
        }
        for(int i=1 ; i<=(R-1)/2 ; i++){
            cout << "D";
            for(int j=1 ; j<C ; j++){
                cout << "L";
            }
            cout << "D";
            for(int j=1 ; j<C ; j++){
                cout << "R";
            }
        }
    }

    // for(int i=1 ; i<=R ; i++){
    //     for(int j=1 ; j<=C ; j++){
    //         cout << map[i][j] << " ";
    //     }
    //     cout << "\n";
    // }

    return 0;
}