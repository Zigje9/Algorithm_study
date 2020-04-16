#include <iostream>

using namespace std;

int DP[101][10];
int N;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    DP[1][0] = 0;
    DP[1][1] = 1;
    DP[1][2] = 1;
    DP[1][3] = 1;
    DP[1][4] = 1;
    DP[1][5] = 1;
    DP[1][6] = 1;
    DP[1][7] = 1;
    DP[1][8] = 1;
    DP[1][9] = 1;

    for(int i=2 ; i<101 ; i++){
        for(int j=0 ; j<10 ; j++){
            if(j==0){
                DP[i][j] = DP[i-1][j+1];
            }
            else if(j==9){
                DP[i][j] = DP[i-1][j-1];
            }
            else{
                DP[i][j] = DP[i-1][j-1]+DP[i-1][j+1];
            }
        }
    }
    long long int sum = 0;
    for(int i=0 ; i<10 ; i++){
        sum += DP[N][i];
    }
    cout << sum%1000000000 ;
    return 0;
}