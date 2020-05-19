#include <iostream>
#include <string>

using namespace std;
string alphabet;
char X;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> alphabet;
    for(int i=0 ; i<26 ; i++){
        X = i + 'a';
        for(int j=0 ; j<alphabet.size() ; j++){
            if(alphabet[j]==X){
                cout << j << " ";
                break;
            }
            if(j==alphabet.size()-1){
                cout << -1 << " ";
            }
        }
    }

    return 0;
}