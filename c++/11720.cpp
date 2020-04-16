#include <iostream>
#include <string.h>

using namespace std;
int N, sum;
string numbers;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    cin >> numbers;
    for(int i=0 ; i<N ; i++){
        sum += numbers[i] - '0';
    }
    cout << sum << endl;
    return 0;
}