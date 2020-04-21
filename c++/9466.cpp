#include <iostream>
#include <string.h>

using namespace std;

int where[100001];
int cycle[100001];
bool visit[100001];
int T,N,cnt;

void dfs(int start){
    visit[start]=true;
    int next = where[start];
    if(visit[next]==false){
        dfs(next);
    }
    else if(cycle[next]==0){
        for(int i=next ; i!=start ; i=where[i]){
            cnt++;
        }
        cnt++;
    }
    cycle[start]=1;
}

int main(){
    scanf("%d",&T);
    while(T-->0){
        scanf("%d",&N);
        for(int i=1 ; i<=N ; i++){
            scanf("%d",&where[i]);
        }
        cnt=0;
        for(int i=1 ; i<=N ; i++){
            if(visit[i]==false){
                dfs(i);
            }
        }
        printf("%d\n",N-cnt);

        memset(where,0,sizeof(where));
        memset(cycle,0,sizeof(cycle));
        memset(visit,false,sizeof(visit));
    }

    return 0;
}