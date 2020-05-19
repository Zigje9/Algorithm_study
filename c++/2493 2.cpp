#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;
vector<pair<int,int>> v;
int N;

void top_control(int b, int i){
    while(!v.empty()){
        if(v.back().first>b){
            printf("%d ",v.back().second);
            v.push_back(make_pair(b,i));
            break;
        }
        else{
            v.pop_back();
            if(v.empty()){
                v.push_back(make_pair(b,i));
                printf("%d ",0);
                break;
            }
        }
    }
}

int main(){
    scanf("%d",&N);
    int a;
    scanf("%d",&a);
    v.push_back(make_pair(a,1));
    printf("%d ",0);

    for(int i=2 ; i<=N ; i++){
        int b;
        scanf("%d",&b);
        top_control(b,i);
    }
    return 0;
}