#include <iostream>
using namespace std;

int N;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    for(int i=1 ; i<=N ; i++){
        for(int j=1 ; j<=i ; j++){
            cout << "*";
        }
        for(int j=N-1 ; j>=i ; j--){
            cout << "  ";
        }
        for(int j=1 ; j<=i ; j++){
            cout << "*";
        }
        cout << endl;
    }

    for(int i=1 ; i<=N ; i++){
        for(int j=N-1 ; j>=i ; j--){
            cout << "*";
        }
        for(int j=1 ; j<=i ; j++){
            cout << "  ";
        }
        for(int j=N-1 ; j>=i ; j--){
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}