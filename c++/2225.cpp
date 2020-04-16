#include <iostream>

using namespace std;
long long int DP[501][501]; 
int N, K;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> K;
    for(int i=1 ; i<=500 ; i++){
        DP[i][0] = 1;
        DP[i][i] = 1;
    }
    for(int i=2; i<=500 ; i++){
        for(int j=1; j<i ; j++){
            DP[i][j] = (DP[i-1][j-1] + DP[i-1][j])%1000000000;
        }
    }
    cout << DP[K+N-1][N];
    return 0;
}