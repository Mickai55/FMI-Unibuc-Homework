#include <iostream>
#include <string.h>
using namespace std;

struct tree
{
    char cuv[100];
    tree *left,*right;
}*root;

tree* inserare (tree *&root,char *x)
{
    if (root==NULL)
    {
        root=new tree;
        strcpy(root->cuv,x);
        root->left=NULL;
        root->right=NULL;
    }
    else if (strcmp (x,root->cuv)<0)
        root->right = inserare (root->right,x);
    else if (strcmp (x,root->cuv)>0)
        root->left = inserare (root->left,x);
    return root;
}

void RSD (tree *root)
{
    if (root!=NULL)
    {
        cout<<root->cuv<<" ";
        RSD (root->left);
        RSD (root->right);
    }
}

void SRD (tree *root)
{
    if (root!=NULL)
    {
        SRD (root->left);
        cout<<root->cuv<<" ";
        SRD (root->right);
    }
}

int main()
{
    inserare (root,"pula");
    inserare (root,"coita");
    inserare (root,"caca");
    inserare (root,"muie");
    inserare (root,"abc");
    RSD(root);
    cout<<endl;
    SRD(root);

    return 0;
}
