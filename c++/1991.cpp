#include <iostream>

using namespace std;

struct Node{
    char value;
    Node *left;
    Node *right;
};

Node *tree;
int N;

void preorder(Node *start){
    cout << start->value;
    if(start->left){
        preorder(start->left);
    }
    if(start->right){
        preorder(start->right);
    }
}

void inorder(Node *start){
    if(start->left){
        inorder(start->left);
    }
    cout << start->value;
    if(start->right){
        inorder(start->right);
    }
}

void postorder(Node *start){
    if(start->left){
        postorder(start->left);
    }
    if(start->right){
        postorder(start->right);
    }
    cout << start->value;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    tree = (Node*)malloc(sizeof(Node)*N);
    char v,l,r;
    for(int i=1 ; i<=N ; i++){
        cin >> v >> l >> r;
        tree[v-'A'].value=v;
        if(l=='.'){
            tree[v-'A'].left=NULL;
        }
        else{
            tree[v-'A'].left=&tree[l-'A'];
        }
        if(r=='.'){
            tree[v-'A'].right=NULL;
        }
        else{
            tree[v-'A'].right=&tree[r-'A'];
        }
    }

    preorder(&tree[0]);
    cout << "\n";
    inorder(&tree[0]);
    cout << "\n";
    postorder(&tree[0]);
    free(tree);
    return 0;
}