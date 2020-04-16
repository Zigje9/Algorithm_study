#include <iostream>
#include <stack>

using namespace std;
long long N;
int B;
stack<long long> s;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> B;
    if(N<B){
        if(N>=10){
            char L = N-10+'A';
            cout << L;
        }
        else{
            cout << N;
        }
        return 0;
    }
    while(N>=B){
        s.push(N%B);
        N=N/B;
    }
    s.push(N);
    long long C = s.size();
    for(long long i=0 ; i<C ; i++){
        if(s.top() >= 10){
            char K = s.top()-10+'A';
            cout << K;
            s.pop();
        }
        else{
            cout << s.top();
            s.pop();
        }
    }
    
    return 0;
}