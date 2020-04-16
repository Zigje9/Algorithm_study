#include <iostream>

using namespace std;

bool prime[1000001];
int M,N;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M >> N;
    for(int i=4 ; i<1000001 ; i=i+2){
        prime[i]=true;
    }
    for(int i=3 ; i<1000001 ; i=i+2){
        if(i*i<1000001){
            for(int j=i*i ; j<1000001 ; j=j+i){
                prime[j] = true;
            }
        }
        else{
            break;
        }
    }
    if(M==1){
        M=2;
    }
    for(int i=M ; i<=N ; i++){
        if(prime[i]==false){
            cout << i << "\n";
        }
    }
    return 0;
}