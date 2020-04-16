#include <iostream>

using namespace std;
int N;
long long int DP[91];
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    DP[1] = 1;
    DP[2] = 1;

    for(int i=3 ; i<=N ; i++){
        DP[i] = DP[i-2] + DP[i-1];
    }

    cout << DP[N];
    return 0;
}