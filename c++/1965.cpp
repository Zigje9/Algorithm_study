#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> v;
int N,a,b;

int main(){
    ios::sync_with_stdio(0);
	cin.tie(0);
    cin >> N;
    cin >> a;
    v.push_back(a);
    for(int i=0 ; i<N-1 ; i++){
        cin >> b;
        if(v.back()<b){
            v.push_back(b);
        }
        else{
            vector<int>::iterator iter = lower_bound(v.begin(), v.end(), b);
            v[iter-v.begin()] = b;
        }
    }
    cout << v.size() << endl;

    return 0;
}