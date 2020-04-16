#include <iostream>
#include <string>

using namespace std;

string line;
int temp = 1;
int answer = 0;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> line;
    for(int i=1 ; i<line.size() ; i++){
        if(line[i]=='('){
            temp += 1;
        }
        else{
            if(line[i-1]=='('){
                temp -= 1;
                answer += temp;
            }
            else{
                answer += 1;
                temp -= 1;
            }
        }
    }

    cout << answer << "\n";

    return 0;
}