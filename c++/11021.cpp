#include <iostream>

using namespace std;
int N,A,B;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    for(int i=0 ; i<N ; i++){
        cin >> A >> B;
        cout << "Case" << " " << "#" << i+1 << ":" << " " << A+B << endl;
    }


    return 0;
}