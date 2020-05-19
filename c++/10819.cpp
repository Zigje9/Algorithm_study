#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>

using namespace std;
int N;
vector<int> v;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i=0 ; i<N ; i++){
        int k;
        cin >> k;
        v.push_back(k);
    }

    sort(v.begin(),v.end());
    int max = 0;
    do{
        int temp = 0;
        for(int i=0 ; i<N-1 ; i++){
            temp += abs(v[i]-v[i+1]);
        }
        if(max < temp){
            max = temp;
        }
    }while(next_permutation(v.begin(),v.end()));

    cout << max;

    return 0;
}