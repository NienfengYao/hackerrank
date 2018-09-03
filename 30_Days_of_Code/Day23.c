#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Node{
    struct Node* left;
    struct Node* right;
    int data;
}Node;
Node* newNode(int data){
    Node* node=(Node*)malloc(sizeof(Node));
    node->left=node->right=NULL;
    node->data=data;
    return node;
}

void levelOrder(Node* root){
  //Write your code here
    Node* queue[1000];
    int head = 0, tail = 0;
    
    if(root)
        queue[tail++] = root;
    
    while(tail > head){
        if(queue[head]->left)
            queue[tail++] = queue[head]->left;
        if(queue[head]->right)
            queue[tail++] = queue[head]->right;
        printf("%d ", queue[head++]->data);

    }
}

Node* insert(Node* root,int data){
    if(root==NULL)
        return newNode(data);
    else{
        Node* cur;
        if(data<=root->data){
            cur=insert(root->left,data);
            root->left=cur;                
        }
        else{
            cur=insert(root->right,data);
            root->right=cur;
        }
        
    }
    return root;
}

int main(){
    Node* root=NULL;
    int T,data;
    scanf("%d",&T);
    while(T-->0){
        scanf("%d",&data);
        root=insert(root,data);
    }
    levelOrder(root);
    return 0;
    
}
