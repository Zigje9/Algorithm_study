#include <iostream>
#include <list>

using namespace std;
list<int> ll;
int N, K;
int answer[5000];
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> K;
    for(int i=1 ; i<=N ; i++){
        ll.push_back(i);
    }
    auto cursor = ll.begin();
    int i = 0;
    while(!ll.empty()){
        for(int j=0 ; j<K ; j++){
            if(cursor==ll.end()){
                cursor=ll.begin();
                cursor++;
            }
            else{
                cursor++;
            }
        }
        cursor--;
        answer[i] = *cursor;
        i++;
        cursor = ll.erase(cursor);
    }

    
    cout << "<";
    for(int i=0 ; i<N-1 ; i++){
        cout << answer[i] << ", ";
    }
    cout << answer[N-1] << ">";
    return 0;
}