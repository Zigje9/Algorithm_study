#include <iostream>

using namespace std;
int N;
int DP[100001];
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    int a;
    cin >> DP[1];
    for(int i=2 ; i<=N ; i++){
        cin >> a;
        if(DP[i-1]<=0){
            DP[i] = a;
        }
        else{
            DP[i] = DP[i-1] + a;
        }
    }
    int answer = DP[1];
    for(int i=1 ; i<=N ; i++){
        if(answer<=DP[i]){
            answer=DP[i];
        }
    }
    cout << answer << "\n";
    return 0;
}