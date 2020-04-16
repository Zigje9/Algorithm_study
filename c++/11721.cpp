#include <iostream>
#include <string.h>

using namespace std;
string word;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> word;
    int N = word.length();
    int M = N/10 + 1;
    for(int i=0 ; i<M ; i++){
        for(int j=i*10 ; j<i*10+10 ; j++){
            if(word[j]==NULL){
                break;
            }
            cout << word[j];
        }
        cout << endl;
    }

    return 0;
}