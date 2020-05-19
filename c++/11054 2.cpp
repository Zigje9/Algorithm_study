#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> v1;
vector<int> v2;

int DATA[1001];
int DP_L[1001];
int DP_R[1001];
int N, b;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int a;
    cin >> N;
    cin >> a;
    v1.push_back(a);
    DATA[N] = a;
    DP_L[1] = 1;
    for(int i=2 ; i<=N ; i++){
        cin >> b;
        DATA[N-i+1] = b;
        if(v1.back()<b){
            v1.push_back(b);
        }
        else{
            vector<int>::iterator iter1 = lower_bound(v1.begin(),v1.end(),b);
            v1[iter1-v1.begin()] = b;
        }
        DP_L[i]=v1.size();
    }

    v2.push_back(DATA[1]);
    DP_R[N] = 1;
    for(int i=2 ; i<=N ; i++){
        if(v2.back()<DATA[i]){
            v2.push_back(DATA[i]);
        }
        else{
            vector<int>::iterator iter2 = lower_bound(v2.begin(),v2.end(),DATA[i]);
            v2[iter2-v2.begin()] = DATA[i];
        }
        DP_R[N-i+1]=v2.size();
    }
    int answer = 0;
    for(int i=1 ; i<=N ; i++){
        if(answer<DP_L[i]+DP_R[i]){
            answer = DP_L[i]+DP_R[i];
        }
    }
    cout << answer-1 << "\n";

    return 0;
}