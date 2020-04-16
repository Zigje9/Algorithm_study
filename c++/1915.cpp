#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

int DP[1001][1001];
int N,M;
int MAP[1001][1001];

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    for(int i=1 ; i<=N ; i++){
        for(int j=1 ; j<=M ; j++){
            int a;
            scanf("%1d",&a);
            MAP[i][j] = a;
        }
    }

    for(int i=1 ; i<=M ; i++){
        DP[1][i] = MAP[1][i];
    }
    for(int i=1 ; i<=N ; i++){
        DP[i][1] = MAP[i][1];
    }

    for(int i=2 ; i<=N ; i++){
        for(int j=2 ; j<=M ; j++){
            if(MAP[i][j]==0){
                DP[i][j]=0;
            }
            else{
                DP[i][j]=min(min(DP[i-1][j-1],DP[i-1][j]),DP[i][j-1])+1;
            }
        }
    }

    int answer = 0;
    for(int i=1 ; i<=N ; i++){
        for(int j=1 ; j<=M ; j++){
            if(answer<DP[i][j]){
                answer = DP[i][j];
            }
        }
    }
    cout << answer*answer;
    return 0;
}