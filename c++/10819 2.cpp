#include <iostream>
#include <vector>

using namespace std;

int N;
int a;
vector<int> v;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i=0 ; i<N ; i++){
        cin >> a;
        v.push_back(a);
    }

    return 0;
}