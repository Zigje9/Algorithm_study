#include <iostream>
#include <deque>
#include <string>

using namespace std;
deque<int> d;
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
        if(line=="push_front"){
            cin >> num;
            d.push_front(num);
        }
        else if(line=="push_back"){
            cin >> num;
            d.push_back(num);
        }
        else if(line=="front"){
            if(!d.empty()){
                cout << d.front() << "\n";
            }
            else{
                cout << "-1" << "\n";
            }
        }
        else if(line=="pop_front"){
            if(!d.empty()){
                cout << d.front() << "\n";
                d.pop_front();
            }
            else{
                cout << "-1" << "\n";
            }
        }
        else if(line=="pop_back"){
            if(!d.empty()){
                cout << d.back() << "\n";
                d.pop_back();
            }
            else{
                cout << "-1" << "\n";
            }
        }
        else if(line=="size"){
            cout << d.size() << "\n";
        }
        else if(line=="empty"){
            cout << d.empty() << "\n";
        }
        else if(line=="back"){
           if(!d.empty()){
                cout << d.back() << "\n";
            }
            else{
                cout << "-1" << "\n";
            }
        }
    }
    return 0;
}