#include <iostream>
#include <algorithm>

using namespace std;
int N, M;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    if(N >= 3){
        if(M >= 7){
            cout << M-2;
            return 0;
        }
        else if(1<=M && M<=4){
            cout << M;
            return 0;
        }
        else{
            cout << 4;
            return 0;
        }
    }

    if(N == 1){
        cout << 1;
        return 0;
    }

    if(N == 2){
        if(M<=2){
            cout << 1;
            return 0;
        }
        else if(3<=M && M<=4){
            cout << 2;
            return 0;
        }
        else if(5<=M && M<=6){
            cout << 3;
            return 0;
        }
        else{
            cout << 4;
            return 0;
        }
    }
    return 0;
}