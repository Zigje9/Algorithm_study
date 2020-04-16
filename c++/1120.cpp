#include <iostream>
#include <string.h>

using namespace std;
string A,B;
int main(){
    cin >> A >> B;
    int maxoverlap = 0;
    for(int i=0 ; i<B.size()-A.size()+1 ; i++){
        int k = i;
        int overlap = 0;
        for(int j=0 ; j<A.size() ; j++){
            if(B[k] == A[j]){
                overlap += 1;
            }
            k += 1;
        }
        if (maxoverlap < overlap){
            maxoverlap = overlap;
        }
    }
    cout << A.size()-maxoverlap ;
    return 0;
}