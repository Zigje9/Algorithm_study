#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, a;
    int min = 1000001;
    int max = -1000001;
    cin >> N;
    for(int i=0 ; i<N ; i++){
        cin >> a;
        if(a<min){
            min = a;
        }
        if(a>max){
            max = a;
        }
    }
    cout << min << " " << max;

    return 0;
}