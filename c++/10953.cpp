#include <iostream>

using namespace std;
int N,A,B;
char C;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    for(int i=0 ; i<N ; i++){
        cin >> A >> C >> B;
        cout << A+B << endl;
    }
}
