#include <iostream>
using namespace std;
int T;
int N;

int gcd(int a, int b){
    if(a<b){
        int temp = a;
        a = b;
        b = temp;
    }
    while(b!=0){
        int r = a%b;
        a = b;
        b = r;
    }
    return a;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    while(T--!=0){
        cin >> N;
        long long sum = 0;
        int arr[101] = {0,};
        for(int i=0 ; i<N ; i++){
            cin >> arr[i];
        }
        for(int i=0 ; i<N-1 ; i++){
            for(int j=i+1 ; j<N ; j++){
                sum += gcd(arr[i],arr[j]);
            }
        }
        cout << sum << "\n";
    }
    return 0;
}