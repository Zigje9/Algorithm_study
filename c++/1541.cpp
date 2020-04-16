#include <iostream>
#include <string.h>
using namespace std;

string str;

int main(){
    string num;
    bool haveMinus = false;
    cin >> str;
    int sic = str.size();
    int sum = 0;

    for(int i=0;i<sic+1;i++){
        if(!(str[i]>=48 && str[i]<=57)){
            if(haveMinus == false){
                sum += stoi(num);
            }
            else{
                sum -= stoi(num);
            }

            if(str[i]==45){
                haveMinus = true;
            }
            num = "";
        }
        else{
            num += str[i];
        }

    }
    cout << sum;
    return 0;
}
