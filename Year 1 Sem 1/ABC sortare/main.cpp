#include <iostream>
using namespace std;

struct tree
{
    int val;
    tree *left,*right;
}*root;

int p=0,x[100];

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

void RSD (tree *root)
{
    if (root!=NULL)
    {
        cout<<root->val<<" ";
        RSD (root->left);
        RSD (root->right);
    }
}

void sortare (tree *root)
{
    if (root!=NULL)
    {
        sortare (root->left);
        x[p]=root->val;
        p++;
        sortare (root->right);
    }
}

int main()
{
    int n,i;
    cin>>n;
    for (i=0;i<n;i++){
        cin>>x[i];
        inserare (root,x[i]);
    }
    sortare(root);
    for (i=0;i<p;i++)
        cout<<x[i]<<" ";

    return 0;
}
