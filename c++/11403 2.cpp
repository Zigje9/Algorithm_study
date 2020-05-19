#include <iostream>
#include <vector>
#include <queue>
#incldue <memory.h>

using namespace std;

int arr[101][101];
vector<int> v[101];
bool visit[101];

bool BFS(int sNode,int eNode){
    queue<int> q;
    q.push(sNode);
    memset(visit, false, sizeof(visit));
    while(!q.empty()){
        int currentNode = q.front(); 
        q.pop();
        for(int i=0 ; i < v[currentNode].size() ; i++){
            int nextNode = v[currentNode][i];
            if(visit[nextNode] != true){
                q.push(nextNode);
                visit[nextNode] = true;
            }

        }
    }
    if(visit[eNode] == false){
        return false;
    }
    else{
        return true;
    }
}

int main(){
    int N;
    cin >> N;
    for(int i=1 ; i < N+1 ; i++){
        for(int j=1 ; j < N+1 ; j++){
            cin >> arr[i][j];
            if(arr[i][j]==1){
                v[i].push_back(j);
            }
        }
    }
    
    for(int i=1 ; i < N+1 ; i++){
        for(int j=1 ; j < N+1 ; j++){
            if(!BFS(i,j)){
                cout << 0 << " ";
            }
            else{
                cout << 1 << " ";
            }
        }
        cout << endl;
    }
}
