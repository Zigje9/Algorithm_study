#include <iostream>
#include <memory.h>
#include <vector>
#include <algorithm>
using namespace std;
vector<pair<int,int>> v;

int testcase;

int newman(){
    v.clear();
    int men = 0;
    int fail = 0;
    int answer = 1;
    cin >> men;
    int a, b;
    for(int i=0 ; i<men ; i++){
        cin >> a >> b;
        v.push_back(make_pair(a,b));
    }
    sort(v.begin(),v.end());
    int compare = v.front().second;
    for(int i=1 ; i<men ; i++){
        if(v[i].second < compare){
            answer += 1;
            compare = v[i].second;
        }
    }
    
    return answer;
}

int main(){
    cin >> testcase;
    for(int i=0 ; i<testcase ; i++){
        cout << newman() << endl;
    }

    return 0;
}