#include <iostream>
#include <queue>
#include <string>

using namespace std;
queue<int> q;
string line;
int N, num, temp;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    fflush(stdin);
    for(int i=0 ; i<N ; i++){
        cin >> line;
        if(line=="push"){
            cin >> num;
            q.push(num);
        }
        else if(line=="front"){
            if(!q.empty()){
                cout << q.front() << "\n";
            }
            else{
                cout << "-1" << "\n";
            }
        }
        else if(line=="pop"){
            if(!q.empty()){
                cout << q.front() << "\n";
                q.pop();
            }
            else{
                cout << "-1" << "\n";
            }
        }
        else if(line=="size"){
            cout << q.size() << "\n";
        }
        else if(line=="empty"){
            cout << q.empty() << "\n";
        }
        else if(line=="back"){
           if(!q.empty()){
                cout << q.back() << "\n";
            }
            else{
                cout << "-1" << "\n";
            }
        }
    }
    return 0;
}