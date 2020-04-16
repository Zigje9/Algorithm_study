#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;
int N;
vector<pair<string,int>> v;

bool compare(pair<string,int>a, pair<string,int>b){
    if(a.second<b.second){
        return true;
    }
    else if (a.second>b.second){
        return false;
    }
    else{
        if(a.first<b.first){
            return true;
        }
        else{
            return false;
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i=0 ; i<N ; i++){
        string str;
        cin >> str;
        v.push_back(make_pair(str,str.size()));
    }

    sort(v.begin(),v.end(),compare);
    cout << v[0].first << "\n";
    for(int i=1 ; i<v.size()-1 ; i++){
        if(v[i].first!=v[i-1].first){
            cout << v[i].first << "\n";
        }
    }
    if(v.size()>2 && v[v.size()-2].first!=v[v.size()-1].first){
        cout << v[v.size()-1].first;
    }



    return 0;
}