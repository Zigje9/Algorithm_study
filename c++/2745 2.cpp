#include <iostream>
#include <cmath>

using namespace std;

string str;
int B;
long long sum = 0;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> str >> B;
    int N = str.size();
    for(int i=N ; i>0 ; i--){
        if('0'<=str[i-1] && str[i-1]<='9'){
            sum += (str[i-1]-'0')*pow(B,N-i);
        }
        else{
            sum += (str[i-1]-'A'+10)*pow(B,N-i);
        }
    }
    cout << sum;

    return 0;
}