#include <iostream>
#include <cmath>
#include <queue>

using namespace std;
string str;
queue<int> s;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> str;
    int N = str.size();
    int A = N/3;  
    int B = N%3;
    int temp;
    if(N==1 && str[0]=='0'){
        cout << 0;
        return 0;
    }
    for(int i=0 ; i<B ; i++){
        temp += (str[i]-'0')*pow(2,B-i-1);
    }
    if(temp!=0){
        s.push(temp);
    }       
    for(int i=0+B ; i<A*3 ; i=i+3){
        temp = (str[i]-'0')*4 + (str[i+1]-'0')*2 + (str[i+2]-'0')*1;
        s.push(temp);
    }
    int K = s.size();
    for(int i=0; i<K ; i++){
        cout << s.front();
        s.pop();
    }

    return 0;
}