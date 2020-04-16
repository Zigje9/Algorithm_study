#include <iostream>
#include <algorithm>
#include <stack>

using namespace std;
int row[11];
stack<int> s;
stack<int> tmp;
int N;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    int a;
    int t;
    for(int i=1 ; i<N+1 ; i++){
        cin >> a;
        row[i] = a;
    }

    for(int i=N ; i>0 ; i--){
        if(row[i] == 0){
            s.push(i);
        }
        else{
            for(int j=0 ; j<row[i] ; j++){
                t = s.top();
                s.pop();
                tmp.push(t);
            }

            s.push(i);

            for(int j=0 ; j<row[i] ; j++){
                t = tmp.top();
                tmp.pop();
                s.push(t);
            }
        }
    }

    for(int i=1 ; i<N+1 ; i++){
        cout << s.top() << " ";
        s.pop();
    }

    return 0;
}