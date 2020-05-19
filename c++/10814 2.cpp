#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<pair<int,int>,string>> v;
int age;
string name;
int N;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i=0 ; i<N ; i++){
        cin >> age >> name;
        v.push_back(make_pair(make_pair(age,i),name));
    }
    sort(v.begin(),v.end());

    for(int i=0 ; i<N ; i++){
        cout << v[i].first.first << " " << v[i].second << "\n";
    }

    return 0;
}