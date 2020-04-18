#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int A,P;
int visit[300001];

void dfs(int start,int P){
    visit[start]++;
    if(visit[start]==3){
        return;
    }
    int next=0 ;
    while(start>0){
        next += (int)pow(start%10,P);
        start = start/10;
    }
    dfs(next,P);
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> A >> P;
    dfs(A,P);
    int cnt = 0;
    for(int i=1 ; i<=300000 ; i++){
        if(visit[i]==1){
            cnt++;
        }
    }
    cout << cnt;
    return 0;
}