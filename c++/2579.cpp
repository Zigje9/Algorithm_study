#include <iostream>
#include <algorithm>

using namespace std;
int DP[301];
int DATA[301];
int N;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i=1 ; i<=N ; i++){
        cin >> DATA[i];
    }
    DP[0] = 0;
    DP[1] = DATA[1];
    DP[2] = DATA[1] + DATA[2];

    for(int i=3 ; i<=N ; i++){
        DP[i] = max(DP[i-2]+DATA[i],DP[i-3]+DATA[i-1]+DATA[i]);
    }
    cout << DP[N] << "\n";

    return 0;
}