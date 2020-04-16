#include <iostream>
using namespace std;
int N;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    if(N==1){
        cout << "*";
        return 0;
    }
    for(int i=1 ; i<=N ; i++){
        for(int j=1 ; j<i ; j++){
            cout << " ";
        }
        for(int j=2*i-1 ; j<=2*N-1 ; j++){
            cout << "*";
        }
        cout << endl;
    }

    for(int i=1 ; i<N ; i++){

        for(int j=i+1 ; j<N ; j++){
            cout << " ";
        }
        for(int j=1 ; j<=2*i+1 ; j++){
            cout << "*";
        }
        if(i == N-1){
            break;
        }
        cout << endl;
    }
    return 0;
}