#include <iostream>
using namespace std;

int T;
int N;
int DP[11];
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    DP[1] = 1;
    DP[2] = 2;
    DP[3] = 4;
    for(int i=4 ; i<=11 ; i++){
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3];
    }
    for(int i=0 ; i<T ; i++){
        cin >> N;
        cout << DP[N] << endl;
    }


    return 0;
}