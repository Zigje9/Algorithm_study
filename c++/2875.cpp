#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N, M, K;
    scanf("%d %d %d",&N, &M, &K);
    if (N%2 != 0){
        N -= 1;
        K -= 1;
        if (N==0){
            cout << 0;
            return 0;
        }
    }
    if (N > M*2){
        K -= (N-M*2);
        N -= N-M*2;
    }
    if (N < M*2){
        K -= (M-N/2);
        M = N/2;
    } 
    if (N+M < K){ 
        cout << 0;
        return 0;
    }

    while(K>0){
        M -= 1;
        K -= 3;
    }
    
    cout << M;

    return 0;
}