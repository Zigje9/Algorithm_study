// 다시 푸세요 .... 갈아엎어서..


#include <iostream>
#include <stdlib.h>

using namespace std;

int N,E;
int up_N,down_N;
int T;
int cnt_up,cnt_down,cnt_100;
bool num_list[10]; //false(0) 인것만 사용 가능 
bool check(int X){
    while(X>0){
        if(num_list[X%10]==true){
            return false;
        }
        else{
            X=X/10;
        }
    }
    return true;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> E;
    for(int i=0 ; i<E ; i++){
        int K;
        cin >> K;
        num_list[K] = true; 
    }
    int Y = N;
    int plus = 0;
    while(Y>0){
        Y=Y/10;
        plus++;
    }
    if(E==0){
        if(N==0){
            cout << 1;
            return 0;
        }
        int NN = 0;
        NN = abs(N-100);
        if(plus>NN){
            cout << NN;
            return 0;
        }
        else{
            cout << plus;
            return 0;
        }
    }
    if(E==10){
        cout << abs(N-100);
        return 0;
    }

    up_N = N;
    down_N = N;
    while(check(up_N)==false){
        cnt_up++;
        up_N++;
        if(up_N==500000){
            break;
        }
    }
    while(check(down_N)==false){
        cnt_down++;
        down_N--;
        if(down_N==0){
            break;
        }
    }
    int change_down=0;
    int change_up=0;
    while(down_N>0){
        down_N = down_N/10;
        change_down++;
    }
    while(up_N>0){
        up_N = up_N/10;
        change_up++;
    }

    cnt_100 = abs(N-100);
    cnt_up += change_up;
    cnt_down += change_down;
    int answer=cnt_100;
    if(answer>cnt_down){
        answer = cnt_down;
    }
    if(answer>cnt_up){
        answer = cnt_up;
    }
    cout << answer;
    return 0;
}