#include <iostream>
#include <vector>


using namespace std;
int N;
int arr[11][11];
int visit[11];
int answer = 999999999;

void dfs(int start, int now, int sum, int count){
    if(count == N && start == now){ 
        if(sum < answer){
            answer = sum;
        } 
        return;
    }
    for(int next=1 ; next<=N ; next++){
        if(arr[now][next]==0) continue;
        if(visit[next]==0 && arr[now][next]!=0){
            visit[next]=1;
            sum += arr[now][next];
            dfs(start, next, sum, count+1);
            visit[next]=0;
            sum -= arr[now][next];
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;

    for(int i=1 ; i<=N ; i++){
        for(int j=1 ; j<=N ; j++){
            cin >> arr[i][j];
        }
    }

    for(int i=1 ; i<=N ; i++){
        dfs(i,i,0,0);
    }

    cout << answer;
    
    return 0;
}