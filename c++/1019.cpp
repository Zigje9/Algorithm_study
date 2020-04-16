#include <iostream>
#include <algorithm>

using namespace std;
int N;
int arr[10];
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    
    int K;
    for(int i=0 ; i<N+1 ; i++){
        int M = i;
        while(M>0){
            arr[M%10] += 1;
            M = M/10;
        }
    }
    for(int i=0 ; i<10 ; i++){
        cout << arr[i] << " ";
    }

    return 0;
}