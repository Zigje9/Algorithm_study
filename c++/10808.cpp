#include <iostream>
#include <string>

using namespace std;
string alphabet;
int atz[26];
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> alphabet;
    for(int i=0 ; i<alphabet.size() ; i++){
        atz[alphabet[i]-'a'] += 1;
    }
    for(int i=0 ; i<26 ; i++){
        cout << atz[i] << " ";
    }
    return 0;
}