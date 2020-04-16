#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> v;
vector<int> va;
int DATA[1001][2];
int N;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    int max = 0;
    for(int i=1 ; i<=N ; i++){
        cin >> DATA[i][0];
    }
    v.push_back(DATA[1][0]);
    DATA[1][1]=0;

    for(int i=2 ; i<=N ; i++){
        if(v.back()<DATA[i][0]){
            v.push_back(DATA[i][0]);
            DATA[i][1] = v.size()-1;
            if(DATA[i][1]>max){
                max=DATA[i][1];
            }
        }
        else{
            vector<int>::iterator iter = lower_bound(v.begin(),v.end(),DATA[i][0]);
            v[iter-v.begin()]=DATA[i][0];
            DATA[i][1] = iter-v.begin();
            if(DATA[i][1]>max){
                max=DATA[i][1];
            }
        }
    }

    while(1){
        if(DATA[N][1]==max){
            break;
        }
        else{
            N--;
        }
    }

    va.push_back(DATA[N][0]);
    int cnt = max-1;
    N--;
    while(cnt>=0){
        if(DATA[N][1]==cnt){
            va.push_back(DATA[N][0]);
            cnt--;
            N--;
        }
        else{
            N--;
        }
    }
    cout << max+1;
    cout << "\n";
    for(int b=va.size()-1 ; b>=0 ; b--){
        cout << va[b] << " ";
    }

    return 0;
}