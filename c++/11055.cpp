#include <iostream>
#include <algorithm>

using namespace std;
int N;
int DP[1001];
int DATA[1001];
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i=1 ; i<=N ; i++){
        cin >> DATA[i];
    }

    for(int i=1 ; i<=N ; i++){
        DP[i] = DATA[i];
        for(int j=1 ; j<i ; j++){
            if(DATA[i] > DATA[j]){
                DP[i] = max(DP[j]+DATA[i],DP[i]);
            }
        }
    }

    int answer = 0;
    for(int i=1 ; i<=N ; i++){
        if(answer < DP[i]){
            answer = DP[i];
        }
    }
    
    cout << answer << "\n";

    return 0;
}