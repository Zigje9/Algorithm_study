#include <iostream>
#include <algorithm>

using namespace std;
int N;
int DP[3][4][3]; // 세로, 가로 , 1최소 2 최대 
int DATA[2][4];

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    cin >> DATA[1][1] >> DATA[1][2] >> DATA[1][3];
    DP[1][1][1] = DATA[1][1];
    DP[1][2][1] = DATA[1][2];
    DP[1][3][1] = DATA[1][3];
    DP[1][1][2] = DATA[1][1];

    DP[1][2][2] = DATA[1][2];

    DP[1][3][2] = DATA[1][3];
    for(int i=2 ; i<=N ; i++){
        cin >> DATA[1][1] >> DATA[1][2] >> DATA[1][3];
        for(int j=1 ; j<4 ; j++){
            if(j==1){
                DP[2][1][1] = min(DP[1][1][1],DP[1][2][1])+DATA[1][1];
                DP[2][1][2] = max(DP[1][1][2],DP[1][2][2])+DATA[1][1];
            }
            else if(j==2){
                DP[2][2][1] = min(min(DP[1][1][1],DP[1][2][1]),DP[1][3][1])+DATA[1][2];
                DP[2][2][2] = max(max(DP[1][1][2],DP[1][2][2]),DP[1][3][2])+DATA[1][2];
            }
            else{
                DP[2][3][1] = min(DP[1][2][1],DP[1][3][1])+DATA[1][3];
                DP[2][3][2] = max(DP[1][2][2],DP[1][3][2])+DATA[1][3];
            }
        }
        DP[1][1][1] = DP[2][1][1];
        DP[1][2][1] = DP[2][2][1];
        DP[1][3][1] = DP[2][3][1];
        DP[1][1][2] = DP[2][1][2];
        DP[1][2][2] = DP[2][2][2];
        DP[1][3][2] = DP[2][3][2];
    }
    cout << max(max(DP[1][1][2],DP[1][2][2]),DP[1][3][2]) << " " << min(min(DP[1][1][1],DP[1][2][1]),DP[1][3][1]);
    return 0;
}