#include <iostream>
#include <string>

using namespace std;
int arr[4] = {0,};

void numline(string L){
    for(int i=0 ; i<L.size() ; i++){
        if('a'<=L[i] && L[i]<='z'){
            arr[0]+=1;
        }
        else if('A'<=L[i] && L[i]<='Z'){
            arr[1]+=1;
        }
        else if('0'<=L[i] && L[i]<='9'){
            arr[2]+=1;
        }
        else{
            arr[3]+=1;
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    while(1){
        string line;
        fflush(stdin);
        getline(cin,line);
        if(line.size()==0){
            break;
        }
        numline(line);
        for(int j=0 ; j<4 ; j++){
            cout << arr[j] << " ";
            arr[j] = 0;
        }
        cout << "\n";
        
    }
    return 0;
}