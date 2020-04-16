#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> v;
int N, f;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    int a;
    cin >> f;
    v.push_back(f);
    for(int i=1 ; i<N ; i++){
        cin >> a;
        if(v.back()<a){
            v.push_back(a);
        }
        else{
            vector<int>::iterator iter = lower_bound(v.begin(),v.end(),a);
            v[iter-v.begin()] = a;
        }
    }
    cout << v.size() << "\n";

    return 0;
}