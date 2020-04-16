#include <iostream>
#include <algorithm>

using namespace std;
int DP[1000001];
int N;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    DP[1] = 0;
    DP[2] = 1;
    cin >> N;
    for(int i=3 ; i<=N ; i++){
        DP[i] = DP[i-1] + 1;
        if(i%2 == 0){
            DP[i] = min(DP[i],DP[i/2]+1);
        }
        if(i%3 == 0){
            DP[i] = min(DP[i],DP[i/3]+1);
        }
    }
    cout << DP[N];
    return 0;
}