#include <iostream>
#include <algorithm>

using namespace std;

int num_of_5(int Num){
    int answer = 0;
    while(1){
        if(Num/5 != 0){
            answer+=Num/5;
            Num = Num/5;
        }
        else{
            break;
        }
    }
    return answer;
}

int num_of_2(int Num){
    int answer = 0;
    while(1){
        if(Num/2 != 0){
            answer+=Num/2;
            Num = Num/2;
        }
        else{
            break;
        }
    }
    return answer;
}

int N,M;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    int R = N-M;
    int K = num_of_2(N)-num_of_2(M)-num_of_2(R);
    int P = num_of_5(N)-num_of_5(M)-num_of_5(R);
    cout << min(K,P) << "\n";
    return 0;
}