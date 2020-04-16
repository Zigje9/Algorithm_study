#include <iostream>

using namespace std;

bool prime[10000001];
int N;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i=4 ; i<10000001 ; i=i+2){
        prime[i] = true;
    }

    for(int i=3 ; i*i<10000001 ; i=i+2){
        if(prime[i]==false){
            for(int j=i*i ; j<10000001 ; j=j+i){
                prime[j] = true;
            }
        }
    }
    if(N==1){
        return 0;
    }
    int k = 2;
    while(1){
        if(N==1){
            break;
        }
        else if(prime[k]==false && N%k==0){
            cout << k << "\n";
            N = N/k;
        }
        else{
            k++;
        }
    }

    return 0;
}