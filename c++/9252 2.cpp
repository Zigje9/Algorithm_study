#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int DP[1001][1001] = {0,};

string A;
string B;
char answer[1001];
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> A >> B;
    for(int i=1 ; i<=B.size() ; i++){
        for(int j=1 ; j<=A.size() ; j++){
            if(B[i-1]==A[j-1]){
                DP[i][j] = DP[i-1][j-1] + 1;
            }
            else{
                DP[i][j] = max(DP[i-1][j],DP[i][j-1]);
            }
        }
    }
    if(DP[B.size()][A.size()] == 0){
        cout << 0;
        return 0;
    }
    int cnt = DP[B.size()][A.size()];
    int i= B.size();
    int j= A.size();
    while(cnt>0){
        if(DP[i][j]!=DP[i-1][j] && DP[i][j]!=DP[i][j-1]){
            answer[cnt]=A[j-1];
            cnt--;
            i-=1;
            j-=1;
        }
        else{
            if(DP[i][j]==DP[i-1][j]){
                i-=1;
            }
            else{
                j-=1;
            }
        }
    }

    cout << DP[B.size()][A.size()] << "\n";
    for(int i=1 ; i<=DP[B.size()][A.size()] ; i++){
        cout << answer[i];
    }
    return 0;
}