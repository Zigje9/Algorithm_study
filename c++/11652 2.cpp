#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<long long> v;
int N;
long long a;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i=0 ; i<N ; i++){
        cin >> a;
        v.push_back(a);
    }
    sort(v.begin(),v.end());
    int cnt = 0;
    int max = 0;
    long long answer = v[0];
    for(int i=1 ; i<N ; i++){
        if(v[i-1]==v[i]){
            cnt += 1;
        }
        else{
            cnt = 0;
        }
        if(cnt>max){
            answer = v[i];
            max = cnt;
        }
    }

    cout << answer << "\n";

    return 0;
}