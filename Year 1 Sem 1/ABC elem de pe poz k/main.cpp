#include <iostream>
using namespace std;

struct tree
{
    int val;
    tree *left,*right;
}*root;

int i=0,k;

tree* inserare (tree *&root, int x)
{
    if (root==NULL)
    {
        root=new tree;
        root->val=x;
        root->left=NULL;
        root->right=NULL;
    }
    else if (x>root->val)
        root->right = inserare (root->right,x);
    else if (x<root->val)
        root->left = inserare (root->left,x);
    return root;
}

void SRD (tree *root, int k1, int k2)
{
    if (root!=NULL)
    {
        SRD (root->left,k1,k2);
        i++;
        if (i==k)
            cout<<root->val<<" ";
        SRD (root->right,k1,k2);
    }
}

int main()
{
    cin>>k;
    inserare (root,4);
    inserare (root,2);
    inserare (root,5);
    inserare (root,1);
    inserare (root,99);
    SRD(root,3,6);

    return 0;
}
