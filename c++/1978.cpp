#include <iostream>

using namespace std;

bool find_num(int a){ //소수면 1 아니면 0
    int i=3;
    while(i<a){
        if(a%i==0){
            return false;
        }
        else{
            i=i+2;
        }
    }
    return true;
}

int N, sum;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    int num;
    for(int i=0 ; i<N ; i++){
        cin >> num;
        if(num%2!=0 && num!=1){
            sum += find_num(num);
        }
        else if(num==2){
            sum += 1;
        }
    }
    cout << sum;
    return 0;
}