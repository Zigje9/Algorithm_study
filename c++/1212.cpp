#include <iostream>

using namespace std;
string answer;
string A;

string find_str(char X){
    if(X=='0'){
        return "000";
    }
    else if(X=='1'){
        return "001";
    }
    else if(X=='2'){
        return "010";
    }
    else if(X=='3'){
        return "011";
    }
    else if(X=='4'){
        return "100";
    }
    else if(X=='5'){
        return "101";
    }
    else if(X=='6'){
        return "110";
    }
    else{
        return "111";
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> A;
    int N = A.size();
    if(N==1 && A[0]=='0'){
        cout << 0;
        return 0;
    }

    if('1'<=A[0] && A[0]<='3'){
        if(A[0]=='1'){
            answer += '1';
        }
        else if(A[0]=='2'){
            answer += "10";
        }
        else{
            answer += "11";
        }
    }
    else{
        answer += find_str(A[0]);
    }

    if(N>=2){
        for(int i=1 ; i<N ; i++){
            answer += find_str(A[i]);
        }
    }

    cout << answer;

    return 0;
}