#include <iostream>
using namespace std;

struct tree{
    int val;
    tree *left,*right;
};

void inserare (int x, tree *&root){
    if (root==NULL){
        root=new tree;
        root->val=x;
        root->left=NULL;
        root->right=NULL;
    }
    else
        if (root->left==NULL&&root->right==NULL)
            inserare (x, root->left);
        else
            inserare (x, root->right);

}

void RSD (tree *root){
    if (root!=NULL){
        cout<<root->val<<" ";
        RSD (root->left);
        RSD (root->right);
    }
}

void SRD (tree *root){
    if (root!=NULL){
        SRD (root->left);
        cout<<root->val<<" ";
        SRD (root->right);
    }
}


int main()
{
    tree *root=NULL;
    int i,n,x;
    cin>>n;
    for (i=0;i<n;i++){
        cin>>x;
        inserare(x,root);
    }
    RSD(root);
    cout<<endl;
    SRD(root);
    cout<<endl;

    return 0;
}
