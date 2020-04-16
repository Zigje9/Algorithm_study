#include <iostream>
#include <algorithm>

using namespace std;
int N;
int DATA[10001];
int DP[10001];
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for(int i=1 ; i<= N ; i++){
        cin >> DATA[i];
    }
    DP[1] = DATA[1];
    for(int i=2 ; i<=N ; i++){
        DP[i] = DATA[i];
        for(int j=1 ; j<i ; j++){
            DP[i] = max(DP[i],DP[i-j]+DATA[j]);
        }
    }

    cout << DP[N];
    return 0;
}