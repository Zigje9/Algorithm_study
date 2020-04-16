#include <iostream>
#include <algorithm>

using namespace std;
long long int DP[10001];
int DATA[10001];
int N;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    int a;
    for(int i=1 ; i<=N ; i++){
        cin >> a;
        DATA[i] = a;
    }
    DP[0] = 0;
    DP[1] = DATA[1];
    DP[2] = DATA[1] + DATA[2];

    for(int j=3 ; j<=N ; j++){
        DP[j] = max(DP[j-2]+DATA[j],DP[j-3]+DATA[j]+DATA[j-1]);
        DP[j] = max(DP[j-1],DP[j]);
    }

    cout << DP[N] << endl;
    return 0;
}