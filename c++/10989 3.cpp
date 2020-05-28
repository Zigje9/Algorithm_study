#include <iostream>

using namespace std;
int arr[10001];
int N,a;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i=0 ; i<N ; i++){
        cin >> a;
        arr[a] += 1;
    }


    for(int i=1 ; i<10001 ; i++){
        if(arr[i] !=0 ){
            for(int j=1 ; j<=arr[i] ; j++){
                cout << i << "\n";
            }
        }
    }

    return 0;
}