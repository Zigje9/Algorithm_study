#include <iostream>
#include <cmath>
#include <stack>

using namespace std;
int A,B;
int m;
int sum;
int temp;
stack<int> s;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> A >> B;
    cin >> m;
    for(int i=0 ; i<m ; i++){
        cin >> temp;
        sum += temp*pow(A,m-i-1); 
    }

    while(sum>=B){
        s.push(sum%B);
        sum = sum/B;
    }
    s.push(sum);
    int N = s.size();
    for(int i=0 ; i<N-1 ; i++){
        cout << s.top() << " ";
        s.pop();
    }
    cout << s.top();
    
    return 0; 
}   