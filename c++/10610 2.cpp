#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string.h>

char arr[100001];
using namespace std;
int main(){
    cin >> arr;
    int len = strlen(arr);
    sort(arr, arr+len);

    if (arr[0] - '0' != 0){
        cout << -1 << endl;
        return 0;
    }
    
    int sum = 0;
    for(int i = 0 ; i < len ; i++){
        sum += arr[i] - '0';
    }

    if (sum % 3 != 0){
        cout << -1 << endl;
        return 0;
    }

    for(int i = len-1; i > -1 ; i--){
        cout << arr[i];
    }

    return 0;
}