#include <iostream>
#include <string.h>

using namespace std;
// 폐급 코드 나중에 다시풀거
int N;
char num_list[10] = {'0','1','2','3','4','5','6','7','8','9'};
char expression[10];
int main(){
    cin >> N;
    for(int i=0 ; i<N ; i++){
        cin >> expression[i];
    }
    int max_stack = 0;
    int end = 0;
    int index = 9;

    for(int i=0 ; i<N ; i++){
        if(expression[i] == '<'){
            max_stack += 1;
        }
        else{
            index -= max_stack;
            for(int j=0 ; j<=max_stack ; j++){
                cout << num_list[index];
                if(j == max_stack){
                    break;
                }
                index += 1;
            }
            index -= (max_stack+1);
            end += max_stack + 1;
            max_stack = 0;
        }
    }
    if(N-end >= 0){
        index = index - (N-end);
        for(int j=0 ; j<N-end+1 ; j++){
            cout << num_list[index];
            index += 1;
        }
    }
    cout << endl;

    index = 0;
    max_stack = 0;
    end = 0;
    for(int i=0 ; i<N ; i++){
        if(expression[i] == '>'){
            max_stack += 1;
        }
        else{
            index += max_stack;
            for(int j=0 ; j<=max_stack ; j++){
                cout << num_list[index];
                if(j == max_stack){
                    break;
                }
                index -= 1;
            }
            index += (max_stack+1);
            end += max_stack + 1;
            max_stack = 0;
        }
    }
    if(max_stack >= 0){
        index = index + max_stack;
        for(int j=0 ; j<max_stack+1 ; j++){
            cout << num_list[index];
            index -= 1;
        }
    }
    
    return 0;
}