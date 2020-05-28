#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;
string arr[1001];
string A;
int main(){
    ios::sync_with_stdio(0);
    cout.tie(0);
    cin.tie(0);
    cin >> A;
    int N  = A.size();
    for(int i=0 ; i<N ; i++){
        arr[i] = A;
        A = A.erase(0,1);
    }
    sort(arr,arr+N);
    for(int i=0 ; i<N ; i++){
        cout << arr[i] << "\n";
    }
    return 0;
}