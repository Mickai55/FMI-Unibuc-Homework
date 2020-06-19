#include <iostream>
using namespace std;

class nod
{
    friend class tree;
public:
    int val;
    nod *left, *right;
}*root;

class tree
{
    public:
    nod* inserare (nod *&root, int x)
    {
        if (root==NULL)
        {
            root = new nod;
            root->val = x;
            root->left = NULL;
            root->right = NULL;
        }
        else if (x > root->val)
            root->right = inserare (root->right, x);
        else if (x < root->val)
            root->left = inserare (root->left, x);
        return root;
    }

    void SRD (nod *root)
    {
        if (root!=NULL)
        {
            SRD (root->left);
            cout<<root->val<<" ";
            SRD (root->right);
        }
    }

    void operator + (int x)
    {
        root = inserare(root, x);
    }

};

int main()
{
    tree t;
    t + 2;
    SRD(t);

    return 0;
}
