#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> v;
int N;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> N;
    int a;
    for(int i=0 ; i<N ; i++){
        cin >> a;
        v.push_back(a);
    }
    sort(v.begin(),v.end());

    int sum = 0;
    
    for(int i=0 ; i<N ; i++){
        if(sum+2 <= v[i]){
            break;
        }
        sum += v[i];
    }

    cout << sum+1 << endl;

    return 0;
}