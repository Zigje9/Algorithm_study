#include <iostream>

using namespace std;

int DP[1001][10];
int N;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;

    DP[1][0] = 1;
    DP[1][1] = 1;
    DP[1][2] = 1;
    DP[1][3] = 1;
    DP[1][4] = 1;
    DP[1][5] = 1;
    DP[1][6] = 1;
    DP[1][7] = 1;
    DP[1][8] = 1;
    DP[1][9] = 1;

    for(int i=2 ; i<=1000 ; i++){
        for(int j=0 ; j<=9 ; j++){
            if(j==0){
                DP[i][j] = DP[i-1][j];
            }
            else{
                for(int k=0; k<=j ; k++){
                    DP[i][j] += DP[i-1][k];
                    DP[i][j] = (DP[i][j]%10007);
                }
            }
        }
    }
    int sum = 0;
    for(int i=0 ; i<10 ; i++){
        sum += DP[N][i];
    }
    cout << sum%10007;
    return 0;
}