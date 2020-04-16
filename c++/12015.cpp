#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int N, a;
vector<int> v;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    cin >> a;
    v.push_back(a);
    int temp;
    for(int i=1 ; i<N ; i++){
        cin >> temp;
        if(v.back()<temp){
            v.push_back(temp);
        }
        else{
            vector<int>::iterator iter = lower_bound(v.begin(),v.end(),temp);
            v[iter-v.begin()]=temp;
        }
    }
    cout << v.size();

    return 0;
}