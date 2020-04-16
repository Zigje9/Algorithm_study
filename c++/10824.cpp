#include <iostream>
#include <string>

using namespace std;
string A;
string B;
string C;
string D;
int main(){
    ios::sync_with_stdio(0);
    cout.tie(0);
    cin.tie(0);
    cin >> A >> B >> C >> D;
    cout << stol(A+B)+stol(C+D);
    return 0;
}