#include<iostream>
#include<fstream>
using namespace std;
class node
{
    friend class BST;
    int data;
    node* left, *right;
};

class BST
{
    node *root;

    node* insert(int x, node* t)
    {
        if(t == NULL)
        {
            t = new node;
            t->data = x;
            t->left = t->right = NULL;
        }
        else if(x < t->data)
            t->left = insert(x, t->left);
        else if(x > t->data)
            t->right = insert(x, t->right);
        return t;
    }

    node* findMin(node* t)
    {
        if(t == NULL)
            return NULL;
        else if(t->left == NULL)
            return t;
        else
            return findMin(t->left);
    }

    node* findMax(node* t)
    {
        if(t == NULL)
            return NULL;
        else if(t->right == NULL)
            return t;
        else
            return findMax(t->right);
    }

    node* remove(int x, node* t)
    {
        node* temp;
        if(t == NULL)
            return NULL;
        else if(x < t->data)
            t->left = remove(x, t->left);
        else if(x > t->data)
            t->right = remove(x, t->right);
        else if(t->left && t->right)
        {
            temp = findMin(t->right);
            t->data = temp->data;
            t->right = remove(t->data, t->right);
        }
        else
        {
            temp = t;
            if(t->left == NULL)
                t = t->right;
            else if(t->right == NULL)
                t = t->left;
            delete temp;
        }

        return t;
    }

    void inorder(node* t)
    {
        if(t == NULL)
            return;
        inorder(t->left);
        cout << t->data << " ";
        inorder(t->right);
    }

    int maxDepth(node* node)
    {
        if (node==NULL)
           return 0;
        else
        {
           int lDepth = maxDepth(node->left);
           int rDepth = maxDepth(node->right);

           if (lDepth > rDepth)
               return(lDepth+1);
           else return(rDepth+1);
        }
    }

    void leaves(node* t)
    {
        if(t == NULL)
            return;
        if (t -> left == NULL && t -> right == NULL)
            cout << t->data << " ";
        leaves(t -> left);
        leaves(t -> right);
    }

    node* makeEmpty(node* t)
    {
        if(t == NULL)
            return NULL;
        {
            makeEmpty(t->left);
            makeEmpty(t->right);
            delete t;
        }
        return NULL;
    }

public:

    BST()
    {
        root = NULL;
    }

    ~BST()
    {
        root = makeEmpty(root);
    }

    friend istream &operator>> (istream &in, BST &t)
    {
        int n, x;
        in >> n;
        for (int i = 0; i < n; i++)
        {
            in >> x;
            t + x;
        }
    }

    void operator + (int x)
    {
        root = insert (x, root);
    }

    void leaves()
    {
        cout << "Frunzele arborelui sunt : ";
        leaves(root);
        cout << endl;
    }

    void remove(int x)
    {
        root = remove(x, root);
        cout << "Se sterge nodul " << x <<"." << endl << endl;
    }

    void height()
    {
        cout << "Inaltimea arborelui este: ";
        cout << maxDepth(root);
        cout << endl << endl;
    }

    void print(ostream &out, node *curr)
    {
        if(curr)
        {
            print(out, curr->left);
            out << curr->data << " ";
            print(out, curr->right);
        }
    }

    friend ostream & operator<<(ostream &out, BST &t)
    {
        out << "Parcurgerea in inordine a arborelui este : ";
        t.print(out, t.root);
        out << endl << endl;

        return out;
    }

};

int main()
{
    ifstream fin ("date.in");

    BST t;

    fin >> t;

    cout << t;

    t.height();

    t.remove (23);

    cout << t;

    t.leaves();
}
