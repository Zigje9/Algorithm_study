#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<long long> v;
int N;
long long a,K;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> K;
    for(int i=0 ; i<N ; i++){
        cin >> a;
        v.push_back(a);
    }
    sort(v.begin(),v.end());

    cout << v[K-1] << "\n";

    return 0;
}