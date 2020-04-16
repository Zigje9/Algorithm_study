#include <iostream>
#include <vector>
#include <string>

using namespace std;
int T;
int K;

bool VPS(string L){
    K=0;
    for(int i=0 ; i<L.size() ; i++){
        if(L[i]=='('){
            K+=1;
        }
        else{
            if(K<=0){
                return false;
            }
            else{
                K-=1;
            }
        }
    }
    if(K!=0){
            return false;
        }
    return true;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    for(int i=0 ; i<T ; i++){
        string line;
        cin >> line;
        if(VPS(line)==false){
            cout << "NO" << "\n";
        }
        else{
            cout << "YES" << "\n";
        }
    }
    return 0;
}
