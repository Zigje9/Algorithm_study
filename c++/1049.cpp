#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int N;
int main(){
    int brand;
    int a,b;
    int money = 0;
    cin >> N >> brand;
    int pakage = 1001;
    int single = 1001;

    for(int i=0 ; i<brand ; i++){
        cin >> a >> b;
        if(a < pakage){
            pakage = a;
        }
        if(b < single){
            single = b;
        }
    }

    if(pakage >= single*6){
        cout << N*single;
        return 0;
    }

    int pakage_num = N/6;
    money += pakage_num*pakage;
    N -= pakage_num*6;
    if(N==0){
        cout << money;
        return 0;
    }
    if(N*single < pakage){
        cout << money+N*single;
        return 0;
    }

    cout << money+pakage;

    return 0;
}