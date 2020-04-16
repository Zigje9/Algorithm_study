#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<pair<int,int>> v;
int N;
int x,y;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i=0 ; i<N ; i++){
        cin >> x >> y;
        v.push_back(make_pair(x,y));
    }

    sort(v.begin(),v.end());
    for(int i=0 ; i<N ; i++){
        cout << v[i].first << " " << v[i].second << "\n";
    }

    return 0;
}