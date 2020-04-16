#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
    ios::sync_with_stdio(0);
	cin.tie(0);
    int N;
    cin >> N;
    int a;
    vector<int> v;
    cin >> a;
    v.push_back(a);
    for(int i=1; i<N ; i++){
        cin >> a;
        if(v.back()<a){
            v.push_back(a);
        }
        else{
            vector<int>::iterator iter = lower_bound(v.begin(), v.end(), a);
            v[iter-v.begin()] = a;
        }

    }
    cout << v.size();

    return 0;

}