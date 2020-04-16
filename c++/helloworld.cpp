#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int arr[10][10];
vector<int> v;
vector<int> v3;

ios::sync_with_stdio(0);
	cin.tie(0);


vector<pair<int, int>> v1;
vector<pair<pair<int, int>, pair<int, int>>> v2;

int main()
{
    // cout << "hello world" << endl; 
    // cout << v.size() << endl;
    // v.push_back(1);
    // cout << v.size() << endl ;
    // v.push_back(3);
    
    // int a;
    // cin >> a;

    // int aa[10];
    // for(int i = 0 ; i < 10 ; i++){
    //     cin >> aa[i];
    // }
    // v1.push_back(make_pair(5,4));
    // cout << v1[0].first << ", ";
    // cout << v1[0].second << endl;
    // printf("(%d, %d)\n", v1[0].first, v1[0].second);
    // cout << v1.size() << endl;


    int minNum = 10;
    for(int i = 2 ; i >= 0 ; i--){
        minNum = min(minNum, i);
    }
    int arr[5] = {4,5,3,2,6};
    cout << max({arr}) << endl;

    return 0;
}