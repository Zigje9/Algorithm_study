#include <iostream>

using namespace std;

int N;
int T;
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
    cin >> N;
    for(int i=0 ; i<N ; i++){
        int A,B;
        cin >> A >> B;
        if(A<B){
            T=B;
            B=A;
            A=T;
        }
        cout << lcm(A,B) << "\n";
    }

    return 0;
}