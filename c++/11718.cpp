#include <iostream>
#include <string.h>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string str;
    while(1){
        getline(cin,str);
        if(str==""){
            break;
        }
        cout << str << endl;
    }

    return 0;
}