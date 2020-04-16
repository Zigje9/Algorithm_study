#include <iostream>
#include <string>

using namespace std;
string line;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    fflush(stdin);
    getline(cin,line);
    for(int i=0 ; i<line.size() ; i++){
        if('A'<=line[i] && line[i]<='M'){
            line[i] += 13;
        }
        else if('N'<=line[i] && line[i]<='Z'){
            line[i] -= 13;
        }
        else if('a'<=line[i] && line[i]<='m'){
            line[i] += 13;
        }
        else if('n'<=line[i] && line[i]<='z'){
            line[i] -= 13;
        }
    }
    cout << line;

    return 0;
}