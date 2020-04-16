#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N;
    cin >> N;
    int arr[100000];

    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }
    sort(arr, arr+N);
    int max = 0;
    // for(int i = 0 ; i < N ; i++){
    //     cout << arr[i] << " ";
    // }
    int j = N;
    for(int i = 0 ; i < N ; i++){
        if (max < arr[i]*j){
            max = arr[i]*j;
        }
        j -= 1;
    }

    cout << max << endl;
    return 0;
}