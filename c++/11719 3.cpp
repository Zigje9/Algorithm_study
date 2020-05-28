#include <iostream>
#include <string.h>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string str;
    int cnt = 0;
    while(1){
        if(cnt>100){
            break;
        }
        getline(cin,str);
        cout << str << endl;
        cnt += 1;
    }

    return 0;
}