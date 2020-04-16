#include <iostream>
#include <string.h>
#include <vector>

using namespace std;
string str;
string boom;
vector<char> v;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> str >> boom;
    v.push_back(str[0]);
    if(boom.size()==1 && boom[0]==v[0]){
        v.pop_back();
    }
    for(int i=1 ; i<str.size() ; i++){
           if(str[i]==boom[boom.size()-1] && v.size()>=boom.size()-1){ // 끝글자랑 같을 때,
                int k = v.size()-1;
                int cnt = boom.size()-1;
                for(int j=boom.size()-2 ; j>=0 ; j--){
                    if(v[k]==boom[j]){
                        k--;
                        cnt--;
                    }
                    else{
                        v.push_back(str[i]);
                        break;
                    }
                }
                if(cnt == 0){ // 삭제해야함 
                    for(int l=0 ; l<boom.size()-1 ; l++){
                        v.pop_back();
                    }
                }
           }
           else{
               v.push_back(str[i]);
           }      
    }
    if(v.empty()){
        cout << "FRULA";
        return 0;
    }
    for(int i=0 ; i<v.size() ; i++){
        cout << v[i];
    }

    return 0;
}
