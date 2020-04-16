#include <iostream>

using namespace std;
string numbers;
int DP[5002];
int DATA[5002];
int main(){ 
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> numbers;
    for(int i=0 ; i<numbers.size()+1 ; i++){
        DATA[i+1]=numbers[i]-'0';
    }
    DP[0] = 1;
    DP[1] = 1;
    DATA[0] = 0;
    for(int j=1 ; j<=numbers.size()+1 ; j++){
        if(DATA[j-1]>=3 && DATA[j]==0){
            cout << 0;
            return 0;
        }
        if(DATA[j-1]==0 && DATA[j]==0){
            cout << 0;
            return 0;
        }
    }
    for(int i=2 ; i<=numbers.size()+1 ; i++){
        if(DATA[i] == 0){
            DP[i] = DP[i-1];
        }
        else if(DATA[i-1]*10+DATA[i]<=26 && DATA[i+1]!=0){
            if(DATA[i-1]==0){
                DP[i] = DP[i-1];
            }
            else{
                DP[i] = (DP[i-2] + DP[i-1])%1000000;
            }
        }
        else{
            DP[i] = DP[i-1];
        }
    }
    cout << DP[numbers.size()]%1000000;
    return 0;
}