#include <iostream>
#include <algorithm>

using namespace std;
int DP[5001];
int N;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    DP[3]=1;
    DP[5]=1;
    DP[6]=2;
    DP[8]=2;
    DP[9]=3;
    DP[10]=2;

    for(int i=11 ; i<=5000 ; i++){
        if(DP[i-3]!=0 && DP[i-5]==0){
            DP[i] = DP[i-3]+1;
        }
        else if(DP[i-3]==0 && DP[i-5]!=0){
            DP[i] = DP[i-5]+1;
        }
        else if(DP[i-3]!=0 && DP[i-5]!=0){
            DP[i] = min(DP[i-3],DP[i-5])+1;
        }
        else{
            ;
        }
    }
    cin >> N;
    if(DP[N]==0){
        cout << -1;
        return 0;
    }
    cout << DP[N];

    return 0;
}