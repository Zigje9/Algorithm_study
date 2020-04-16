#include <iostream>
using namespace std;

int N;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    for(int i=0 ; i<N ; i++){
        for(int j=i+1 ; j<N ; j++){
            cout << " ";
        }
        for(int j=2*i ; j>=0; j--){
            if(j%2 == 0){
                cout << "*";
            }
            else{
                cout << " ";
            }
        }
        if(i==N-1){
            break;
        }
        cout << endl;
    }
    return 0;
}