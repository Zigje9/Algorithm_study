#include <iostream>

using namespace std;
long long A;
long long B;
 
long long gcd(long long a, long long b){
    while(b!=0){
        long long r = a%b;
        a = b;
        b = r;
    }
    return a;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> A >> B;
    if(A<B){
        long long temp = A;
        A = B;
        B = temp;
    }
    long long answer = gcd(A,B);
    for(long long i=0 ; i<answer ; i++){
        cout << 1;
    }

    return 0;
}