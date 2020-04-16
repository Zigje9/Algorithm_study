#include <iostream>
#include <string.h>

using namespace std;
char map1[51][51];
char map2[51][51];
int N,M;

void change(int a,int b){
    for(int i=a ; i<a+3 ; i++){
        for(int j=b ; j<b+3 ; j++){
            if(map1[i][j] == 'T'){
                map1[i][j] = 'F';
            }
            else{
                map1[i][j] = 'T';
            } 
        }
    }
}

int main(){
    int T_cnt = 0;
    cin >> N >> M;
    for(int i=0 ; i<N ; i++){
        cin >> map1[i];
    }
    for(int i=0 ; i<N ; i++){
        cin >> map2[i];
    }
    for(int i=0 ; i<N ; i++){
        for(int j=0 ; j<M ; j++){
            if(map1[i][j] == map2[i][j]){
                map1[i][j] = 'T';
            }
            else{
                map1[i][j] = 'F';
            }
        }
    }

    if(N<3 or M<3){
        for(int i=0 ; i<=N ; i++){
            for(int j=0 ; j<=M ; j++){
                if(map1[i][j] == 'F'){
                    cout << -1;
                    return 0;
                }
            }
        }
        cout << 0;
        return 0;
    }

    for(int i=0 ; i<=N-3 ; i++){
        for(int j=0 ; j<=M-3 ; j++){
            if(map1[i][j] == 'F'){
                change(i,j);
                T_cnt += 1;
            }
        }
    }
    for(int i=0 ; i<N ; i++){
        for(int j=0 ; j<M ; j++){
            if(map1[i][j] == 'F'){
                cout << -1;
                return 0;
            }
        }
    }
    cout << T_cnt;
    return 0;
}