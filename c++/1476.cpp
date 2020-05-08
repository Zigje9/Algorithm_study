#include <iostream>

using namespace std;

int E,S,M; //15,28,19

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> E >> S >> M;
    int cnt = 1;
    while(E+S+M!=3){
        if(E!=1){
            E-=1;
        }
        else{
            E=15;
        }
        if(S!=1){
            S-=1;
        }
        else{
            S=28;
        }
        if(M!=1){
            M-=1;
        }
        else{
            M=19;
        }
        cnt++ ;
    }
    cout << cnt;

    return 0;
}