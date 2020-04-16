#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int arr[1001];
vector<int> v;
int N;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i=1 ; i<=N ; i++){
        cin >> arr[N-i+1];
    }
    v.push_back(arr[1]);
    for(int i=2 ; i<=N ; i++){
        if(v.back()<arr[i]){
            v.push_back(arr[i]);
        }
        else{
            vector<int>::iterator iter = lower_bound(v.begin(),v.end(),arr[i]);
            v[iter-v.begin()] = arr[i];
        }
    }
    
    cout << v.size() << "\n";

    return 0;
}