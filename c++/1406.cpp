#include <iostream>
#include <list>

using namespace std;
list<char> ll;
string f;
int T;
char word;
int main(){
    ios::sync_with_stdio(0);
    cout.tie(0);
    cin.tie(0);
    cin >> f;
    int N = f.size();
    for(int i=0 ; i<N ; i++){
        ll.push_back(f[i]);
    }
    auto cursor = ll.end();
    cin >> T;
    for(int i=0 ; i<T ; i++){
        string command;
        fflush(stdin);
        cin >> command;
        if(command == "P"){
            cin >> word;
            if(ll.begin()==ll.end()){
                ll.push_front(word);
            }
            else{
                ll.insert(cursor,word);
            }
        }
        else if(command == "L"){
            if(cursor==ll.begin()){
                ;
            }
            else{ 
                cursor--;
            }
        }
        else if(command == "D"){
            if(cursor == ll.end()){
                ;
            }
            else{
                cursor++;
            }
        }
        else if(command == "B"){
            if(cursor==ll.begin()){
                ;
            }
            else{
                cursor--;
                cursor = ll.erase(cursor);
            }
        }
    }  
    for(const auto& elem : ll){
            cout << elem;
        }
    return 0;
}
