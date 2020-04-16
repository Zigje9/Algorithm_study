#include <iostream>
#include <stack>
#include <string.h>

using namespace std;

string expr;
stack<char> s;

void postfix(int i){
    if(s.empty()){
        s.push(expr[i]);
    }
    else{
        if(43==expr[i] || expr[i]==45){ // + or - 인경우 
            while(1){
                if(s.top()==40){
                    s.push(expr[i]);
                    break;
                }
                else{
                    cout << s.top();
                    s.pop();
                    if(s.empty()){
                        s.push(expr[i]);
                        break;
                    }
                }
            }
        }
        else if(expr[i]==42 || expr[i]==47){ // * or / 인경우
            while(1){
                if(s.top()==43 || s.top()==45){
                    s.push(expr[i]);
                    break;
                }
                else if(s.top()==40){
                    s.push(expr[i]);
                    break;
                }
                else{
                    cout << s.top();
                    s.pop();
                    if(s.empty()){
                        s.push(expr[i]);
                        break;
                    }
                }
            }
        }
        else if(expr[i]==40){ // ( 인경우
            s.push(expr[i]);
        }
        else{ // )인 경우 
            while(s.top()!='('){
                cout << s.top();
                s.pop();
            }
            s.pop();
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> expr;
    for(int i=0 ; i<expr.size() ; i++){
        if(65<=expr[i] && expr[i]<=90){ // 숫자 바로 출력 
            cout << expr[i];
        }
        else{
            postfix(i);
        }
    }
    int k = s.size();
    for(int j=0 ; j<k ; j++){ // 스택에 남은 연산자 처리 
        cout << s.top();
        s.pop();
    }
    cout << "\n";
    return 0;
}