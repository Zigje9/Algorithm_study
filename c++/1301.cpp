#include <iostream>
#include <string.h>

using namespace std;

long long DP[11][11][11][11][11][6][6];
long long answer=0;
int ball[6];
int N;

long long bizz(int a, int b, int c, int d, int e, int pp, int p){
    if(!(a>=0 && b>=0 && c>=0 && d>=0 && e>=0)){
        return 0;
    }
    if(a==0 && b==0 && c==0 && d==0 && e==0){
        return 1;
    }
    long long& iter = DP[a][b][c][d][e][pp][p];
    if(iter != -1){
        return iter;
    }
    iter = 0;
    if(a>=1 && pp!=1 && p!=1){
        iter += bizz(a-1,b,c,d,e,p,1);
    }
    if(b>=1 && pp!=2 && p!=2){
        iter += bizz(a,b-1,c,d,e,p,2);
    }
    if(c>=1 && pp!=3 && p!=3){
        iter += bizz(a,b,c-1,d,e,p,3);
    }
    if(d>=1 && pp!=4 && p!=4){
        iter += bizz(a,b,c,d-1,e,p,4);
    }
    if(e>=1 && pp!=5 && p!=5){
        iter += bizz(a,b,c,d,e-1,p,5);
    }
    return iter;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i=1 ; i<=N ; i++){
        cin >> ball[i];
    }
    memset(DP,-1,sizeof(DP));
    answer = bizz(ball[1],ball[2],ball[3],ball[4],ball[5],0,0);
    cout << answer;

    return 0;
}