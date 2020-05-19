#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;
int T, N;
int DATA[100001][2];
int DP[100001][2];
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    for(int i=0 ; i<T ; i++){
        cin >> N;
        int a;
        memset(DATA,0,sizeof(DATA));
        memset(DP,0,sizeof(DP));
        for(int i=1 ; i<=N ; i++){
            cin >> a;
            DATA[i][0] = a;
        }
        for(int i=1 ; i<=N ; i++){
            cin >> a;
            DATA[i][1] = a;
        }
        DP[1][0] = DATA[1][0];
        DP[1][1] = DATA[1][1];
        DP[2][0] = DATA[1][1] + DATA[2][0];
        DP[2][1] = DATA[1][0] + DATA[2][1];  
        for(int i=3 ; i<=N ; i++){
            DP[i][0] = max(DP[i-1][1],DP[i-2][1])+DATA[i][0];
            DP[i][1] = max(DP[i-1][0],DP[i-2][0])+DATA[i][1];
        }
        cout << max(DP[N][0],DP[N][1]) << endl;
    }


    return 0;
}