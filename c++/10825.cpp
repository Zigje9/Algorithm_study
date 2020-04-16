#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<pair<pair<string,int>,pair<int,int>>> v;
string name;
int kor,eng,math;
int N;

bool compare(pair<pair<string,int>,pair<int,int>> a, pair<pair<string,int>,pair<int,int>> b){
    if(a.first.second == b.first.second){
        if(a.second.first == b.second.first){
            if(a.second.second == b.second.second){
                return a.first.first < b.first.first;
            }
            else{
                return a.second.second > b.second.second;
            }
        }
        else{
            return a.second.first < b.second.first;
        }
    }
    else{
        return a.first.second > b.first.second;
    }
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i=0 ; i<N ; i++){
        cin >> name >> kor >> eng >> math;
        v.push_back(make_pair(make_pair(name,kor),make_pair(eng,math)));
    }

    sort(v.begin(), v.end(), compare);

    for(int i=0 ; i<N ; i++){
        cout << v[i].first.first << "\n";
    }

    return 0;
}