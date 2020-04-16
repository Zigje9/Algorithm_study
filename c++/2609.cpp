#include <iostream>

using namespace std;

int gcd(int a, int b){
    while(b!=0){
        int r = a%b;
        a=b;
        b=r;
    }
    return a;
}

int lcm(int a, int b){
    return a*b/gcd(a,b);
}

int main(){
    ios::sync_with_stdio(0);
    cout.tie(0);
    cin.tie(0);
    int A,B;
    cin >> A >> B;
    int T;
    if(A<B){
        T=B;
        B=A;
        A=T;
    }
    cout << gcd(A,B) << "\n";
    cout << lcm(A,B);

    return 0;
}