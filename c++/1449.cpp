#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> v;
int N, L;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> L;
    if(L==1){
        cout << N;
        return 0;
    }
    int a;
    for(int i=0 ; i<N ; i++){
        cin >> a;
        v.push_back(a);
    }
    sort(v.begin(),v.end());
    int cnt = 1;
    int tmp = v[0]+L-1;
    for(int i=1 ; i<N ; i++){
        if(v[i]>tmp){
            tmp = v[i]+L-1;
            cnt += 1;
        }
    }
    
    cout << cnt << endl;

    return 0;
}
 
