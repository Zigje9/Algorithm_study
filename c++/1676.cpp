#include <iostream>

using namespace std;

int N;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    int answer = 0;

    while(1){
        if(N/5 != 0){
            answer+=N/5;
            N = N/5;
        }
        else{
            break;
        }
    }
    cout << answer;

    return 0;
}