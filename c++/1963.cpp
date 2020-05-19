#include <iostream>
#include <math.h>
#include <queue>
#include <string.h>

using namespace std;

bool prime[10001]; // false -> 소수 
int visit[10001];
int T;
int start_num;
int end_num;

int bfs(){
    memset(visit, 0, sizeof(visit));
    queue<int> q;
    q.push(start_num);
    visit[start_num] = 1;
    while(!q.empty()){
        int temp = q.front();
        q.pop();
        if(temp == end_num){
            return visit[temp]-1;
        }
        else{
            int a = temp/1000;
            int b = (temp - a*1000) / 100;
            int c = (temp - a*1000 - b*100) / 10;
            int d = (temp - a*1000 - b*100 - c*10);
            
            for(int k=1 ; k<=9 ; k=k+2){ // 1의자리 변경 
                int next = temp - d + k;
                if(next != temp && prime[next]==0){
                    if(visit[next]==0){
                        q.push(next);
                        visit[next]=visit[temp]+1;
                    }
                }
            }
            for(int k=0 ; k<=9 ; k++){ // 10의자리 변경 
                int next = temp - c*10 + k*10;
                if(next != temp && prime[next]==0){
                    if(visit[next]==0){
                        q.push(next);
                        visit[next]=visit[temp]+1;
                    }
                }
            }
            for(int k=0 ; k<=9 ; k++){ // 100의자리 변경 
                int next = temp - b*100 + k*100;
                if(next != temp && prime[next]==0){
                    if(visit[next]==0){
                        q.push(next);
                        visit[next]=visit[temp]+1;
                    }
                }
            }
            for(int k=1 ; k<=9 ; k++){ // 1000의자리 변경 
                int next = temp - a*1000 + k*1000;
                if(next != temp && prime[next]==0){
                    if(visit[next]==0){
                        q.push(next);
                        visit[next]=visit[temp]+1;
                    }
                }
            }
        }
    }
    return -1;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    for(int i=2 ; i<=sqrt(10000) ; i++){
        for(int j=i+i ; j<=10000 ; j=j+i){
            prime[j] = true;
        }
    }
    prime[1] = true;
    prime[2] = false;

    cin >> T;
    
    for(int i=1 ; i<=T ; i++){
        cin >> start_num >> end_num;
        int answer = bfs();
        if(answer == -1){
            cout << "impossible" << "\n";
        }
        else{
            cout << answer << "\n";
        }
    }
    return 0;
}