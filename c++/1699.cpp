#include <iostream>
#include <algorithm>

using namespace std;
int DP[100001];
int N;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    DP[1] = 1;
    DP[2] = 2;
    DP[3] = 3;
    for(int i=4 ; i<=N ; i++){
        DP[i] = 4;
        for(int j=2 ; (j*j)<=i ; j++){
            DP[i] = min(DP[i],DP[i-j*j]+1);
        }
    }

    cout << DP[N] << "\n";
    return 0;
}