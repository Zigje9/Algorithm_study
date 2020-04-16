#include <iostream>

using namespace std;

int N;
bool prime[1000001];

int find_sum(int N){
    int mid = N/2;
    for(int i=3 ; i<=mid ; i=i+2){
        if(prime[i]==false){
            if(prime[N-i]==false){
                printf("%d = %d + %d\n",N,i,N-i);
                return 0;
            }
        }
    }
    return 0;
}

int main(){
    prime[1]=true;
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

    while(1){
        scanf("%d",&N);
        if(N==0){
            break;
        }
        find_sum(N);
    }

    return 0;
}