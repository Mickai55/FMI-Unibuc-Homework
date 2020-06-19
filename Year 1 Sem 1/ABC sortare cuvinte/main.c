#include <iostream>
using namespace std;

struct tree
{
    char cuv[100];
    tree *left,*right;
}*root;

tree* inserare (tree *&root,char x[])
{
    if (root==NULL)
    {
        root=new tree;
        root->cuv=x;
        root->left=NULL;
        root->right=NULL;
    }
    else if (x>root->val)
        root->right = inserare (root->right,x);
    else if (x<root->val)
        root->left = inserare (root->left,x);
    return root;
}

int search (tree *root, int x)
{
    if (root==NULL)
        return 0;
    else if (x<root->val)
        return search (root->left,x);
    else if (x>root->val)
        return search (root->right,x);
    else
        return 1;

}

tree* findMax(tree *root)
{
    while (root->right!=NULL)
        root=root->right;
    return root;

}

tree* findMin(tree *root)
{
    while (root->left!=NULL)
        root=root->left;
    return root;

}

tree* remove(int x,tree* root)
{
    tree* temp;
    if(root == NULL)
        return NULL;
    else if(x < root->val)
        root->left = remove(x, root->left);
    else if(x > root->val)
        root->right = remove(x, root->right);
    else if(root->left && root->right)
    {
        temp = findMin(root->right);
        root->val = temp->val;
        root->right = remove(root->val, root->right);
    }
    else
    {
        temp = root;
        if(root->left == NULL)
            root = root->right;
        else if(root->right == NULL)
            root = root->left;
        delete temp;
    }

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

void SRD (tree *root)
{
    if (root!=NULL)
    {
        SRD (root->left);
        cout<<root->val<<" ";
        SRD (root->right);
    }
}

int main()
{
    int x;
    inserare (root,4);
    inserare (root,2);
    inserare (root,5);
    inserare (root,1);
    inserare (root,99);
    remove (1,root);
    RSD(root);
    SRD(root);

    return 0;
}
