#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<int, int>> line;
vector<int> v;
int N, a, b;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;

    for(int i=0 ; i<N ; i++){
        cin >> a >> b;
        line.push_back(make_pair(a, b));
    }

    sort(line.begin(),line.end());

    v.push_back(line[0].second);

    for(int i=1 ; i<N ; i++){
        if(v.back()<line[i].second){
            v.push_back(line[i].second);
        }
        else{
            vector<int>::iterator iter = lower_bound(v.begin(), v.end(), line[i].second);
            v[iter-v.begin()] = line[i].second;
        }
    }

    cout << N-v.size() << endl;

    return 0;
}