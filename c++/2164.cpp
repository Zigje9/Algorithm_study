#include <iostream>
#include <deque>

using namespace std;
deque<int> dq;
int N;
int temp;
int main(){
    cin >> N;
    for(int i=1 ; i<=N ; i++){
        dq.push_back(i);
    }
    while(dq.size()!=1){
        dq.pop_front();
        temp = dq[0];
        dq.push_back(temp);
        dq.pop_front();
    }
    cout << dq[0];

    return 0;
}