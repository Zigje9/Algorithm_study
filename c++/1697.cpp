#include <iostream>
#include <algorithm>

using namespace std;
int N,K;
int DP[100001];
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> K;
    if(N>=K){
        cout << N-K;
        return 0;
    }
    for(int i=0 ; i<=N ; i++){
        DP[i] = N-i;
    }
    DP[N+1]=1;
    for(int i=N+2 ; i<=100000 ; i++){
        if(i%2==0){
            DP[i] = min(DP[i-1]+1,DP[i/2]+1);
        }
        else{
            DP[i] = min(DP[i-1]+1,DP[(i+1)/2]+2);
        }
    }
    cout << DP[K];
    return 0;
}