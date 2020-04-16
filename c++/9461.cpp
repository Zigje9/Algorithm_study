#include <iostream>

using namespace std;
long long int DP[101];
int T, N;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    DP[1]=1;
    DP[2]=1;
    DP[3]=1;
    DP[4]=2;
    DP[5]=2;
    DP[6]=3;
    for(int i=7 ; i<=100 ; i++){
        DP[i] = DP[i-1] + DP[i-5];
    }

    cin >> T;
    while(T-- > 0){
        cin >> N;
        cout << DP[N] << "\n";
    }
 
    return 0;
}