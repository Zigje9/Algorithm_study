#include <iostream>
#include <stack>

using namespace std;
int N;
stack<int> s;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    if(N==0){
        cout << 0 << "\n";
        return 0;
    }

    while(N!=1){
        if(N<0){
            if(N%(-2)==-1){
                s.push(-(N%(-2)));
                N = N/(-2)+1;
            }
            else{
                s.push(0);
                N = N/(-2);
            }
        }
        else{
            s.push(N%(-2));
            N = N/(-2);
        }
    }
    s.push(1);
    int T = s.size();
    for(int i=0 ; i<T ; i++){
        cout << s.top();
        s.pop();
    }
    return 0;
}