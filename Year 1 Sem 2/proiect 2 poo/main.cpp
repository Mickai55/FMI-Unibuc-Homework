#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

template <class T>
class noduri
{
};

class Nod
{
    int val;
    noduri<Nod> *left, *right;
public:
    Nod (int k = 0, Nod *stanga = NULL, Nod *dreapta = NULL)
    {
        val = k;
        left = stanga;
        right = dreapta;
    }
    Nod (Nod &k)
    {
        val = k.val;
        left = k.left;
        right = k.right;
    }
    Nod operator=(Nod k)
    {
        val = k.val;
        left = k.left;
        right = k.right;
    }
    friend istream& operator>>(istream &in, Nod &k)
    {
        in >> k.val;
        return in;
    }
    friend ostream& operator<<(ostream &out, Nod &k)
    {
        out << k.val << '\n';
        return out;
    }
    ~Nod ()
    {
        val = 0;
        left = right = NULL;
    }
    int getVal ()
    {
        return val;
    }
    void setVal (int valoare)
    {
        val = valoare;
    }
    Nod* getLeft()
    {
        return left;
    }
    void setLeft (Nod* stanga)
    {
        left = stanga;
    }
    Nod* getRight()
    {
        return right;
    }
    void setRight (Nod* dreapta)
    {
        right = dreapta ;
    }
};

enum COLOR { RED, BLACK };

class Nod_rosu_negru : Nod
{
    COLOR color;
    Nod_rosu_negru *left, *right, *parent;
    int val = getVal();
public:
    Nod_rosu_negru(int k = 0, Nod_rosu_negru* stanga = NULL, Nod_rosu_negru* dreapta = NULL, Nod_rosu_negru* parinte = NULL)
    {
        parent = parinte;
        left = stanga;
        right = dreapta;
        val = k;
        color = RED;
    }
    Nod_rosu_negru (Nod_rosu_negru &k)
    {
        val = k.val;
        left = k.left;
        right = k.right;
        parent = k.parent;
        color = k.color;
    }
    Nod_rosu_negru operator=(Nod_rosu_negru k)
    {
        val = k.val;
        left = k.left;
        right = k.right;
        parent = k.parent;
        color = k.color;
    }
    friend istream& operator>>(istream &in, Nod_rosu_negru &k)
    {
        in >> k.val;
        return in;
    }
    friend ostream& operator<<(ostream &out, Nod_rosu_negru &k)
    {
        out << k.val << '\n';
        return out;
    }
    int getVal ()
    {
        return val;
    }
    void setVal (int valoare)
    {
        val = valoare;
    }
    Nod_rosu_negru* getLeft()
    {
        return left;
    }
    void setLeft (Nod_rosu_negru* stanga)
    {
        left = stanga;
    }
    Nod_rosu_negru* getRight()
    {
        return right;
    }
    void setRight (Nod_rosu_negru* dreapta)
    {
        right = dreapta ;
    }
    Nod_rosu_negru* getParent()
    {
        return parent;
    }
    void setParent(Nod_rosu_negru *parinte)
    {
        parent = parinte;
    }
    COLOR getColor()
    {
        return color;
    }
    void setColor(COLOR culoare)
    {
        color = culoare;
    }

    Nod_rosu_negru *uncle()
    {
        if (parent == NULL or parent->parent == NULL)
          return NULL;

        if (parent->isOnLeft())
          return parent->parent->right;
        else
          return parent->parent->left;
    }

    bool isOnLeft() { return this == parent->left; }

    Nod_rosu_negru *sibling()
    {
        if (parent == NULL)
            return NULL;

        if (isOnLeft())
            return parent->right;

        return parent->left;
    }

    void moveDown(Nod_rosu_negru *nParent)
    {
        if (parent != NULL) {
            if (isOnLeft())
                parent->left = nParent;
            else
            parent->right = nParent;
        }
        nParent->parent = parent;
        parent = nParent;
    }

    bool hasRedChild()
    {
        return (left != NULL and left->color == RED) or
            (right != NULL and right->color == RED);
    }
};

class Arbore
{
    int nr_noduri;
public:
    Arbore(int nrNoduri = 0)
    {
        nr_noduri = nrNoduri;
    }
    virtual int get_depth()
    {
    }
};

class ABC : Arbore
{
    Nod *root;

    Nod* insert(int x, Nod* t)
    {
        if(t == NULL)
        {
            t =new Nod(x);
        }
        else if(x < t->getVal())
            t->setLeft(insert(x, t->getLeft()));
        else if(x > t->getVal())
            t->setRight(insert(x, t->getRight()));
        return t;
    }

    Nod* findMin(Nod* t)
    {
        if(t == NULL)
            return NULL;
        else if(t->getLeft() == NULL)
            return t;
        else
            return findMin(t->getLeft());
    }

    Nod* findMax(Nod* t)
    {
        if(t == NULL)
            return NULL;
        else if(t->getRight() == NULL)
            return t;
        else
            return findMax(t->getRight());
    }

    Nod* remove(int x, Nod* t)
    {
        Nod* temp;
        if(t == NULL)
            return NULL;
        else if(x < t->getVal())
            t->setLeft(remove(x, t->getLeft()));
        else if(x > t->getVal())
            t->setRight(remove(x, t->getRight()));
        else if(t->getLeft() && t->getRight())
        {
            temp = findMin(t->getRight());
            t->setVal(temp->getVal());
            t->setRight(remove(t->getVal(), t->getRight()));
        }
        else
        {
            temp = t;
            if(t->getLeft() == NULL)
                t = t->getRight();
            else if(t->getRight() == NULL)
                t = t->getLeft();
            delete temp;
        }

        return t;
    }

    void leaves(Nod* t)
    {
        if(t == NULL)
            return;
        if (t->getLeft() == NULL && t->getRight() == NULL)
            cout << t->getVal() << " ";
        leaves(t->getLeft());
        leaves(t->getRight());
    }

    Nod* makeEmpty(Nod* t)
    {
        if(t == NULL)
            return NULL;
        {
            makeEmpty(t->getLeft());
            makeEmpty(t->getRight());
            delete t;
        }
        return NULL;
    }

    int height (Nod *node)
    {
        if (node == NULL)
            return 0;
        int lDepth = height(node->getLeft());
        int rDepth = height(node->getRight());

        if (lDepth > rDepth)
            return(lDepth+1);
        else
            return(rDepth+1);
    }

public:

    ABC()
    {
        root = NULL;
    }

    ~ABC()
    {
        root = makeEmpty(root);
    }

    void operator + (int x)
    {
        root = insert (x, root);
    }

    friend istream &operator>> (istream &in, ABC &t)
    {
        int n, x;
        in >> n;
        for (int i = 0; i < n; i++)
        {
            in >> x;
            t + x;
        }
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

    int get_depth()
    {
        return height(root);
    }

    void printin(ostream &out, Nod *curr)
    {
        if(curr)
        {
            printin(out, curr->getLeft());
            out << curr->getVal() << " ";
            printin(out, curr->getRight());
        }
    }

    void printpre(ostream &out, Nod *curr)
    {
        if(curr)
        {
            out << curr->getVal() << " ";
            printpre(out, curr->getLeft());
            printpre(out, curr->getRight());
        }
    }

    friend ostream & operator<<(ostream &out, ABC &t)
    {
        out << "Parcurgerea in inordine a arborelui este : ";
        t.printin(out, t.root);
        out << '\n' << "Parcurgerea in preordine a arborelui este : ";
        t.printpre(out, t.root);
        out << endl << endl;

        return out;
    }

};

class Arbore_bicolor : Arbore
{
    Nod_rosu_negru *root;

    void leftRotate(Nod_rosu_negru *x)
    {
        Nod_rosu_negru *nParent = x->getRight();

        if (x == root)
            root = nParent;

        x->moveDown(nParent);

        x->setRight(nParent->getLeft());
        if (nParent->getLeft() != NULL)
            nParent->getLeft()->setParent(x);

        nParent->setLeft(x);
    }

    void rightRotate(Nod_rosu_negru *x)
    {
        Nod_rosu_negru *nParent = x->getLeft();

        if (x == root)
            root = nParent;

        x->moveDown(nParent);

        x->setLeft(nParent->getRight());
        if (nParent->getRight() != NULL)
            nParent->getRight()->setParent(x);

        nParent->setRight(x);
    }

    void swapColors(Nod_rosu_negru *x1, Nod_rosu_negru *x2)
    {
        COLOR temp;
        temp = x1->getColor();
        x1->setColor(x2->getColor());
        x2->setColor(temp);
    }

    void swapValues(Nod_rosu_negru *u, Nod_rosu_negru *v)
    {
        int temp;
        temp = u->getVal();
        u->setVal(v->getVal());
        v->setVal(temp);
    }

    void fixRedRed(Nod_rosu_negru *x)
    {
        if (x == root)
        {
            x->setColor(BLACK);
            return;
        }

        Nod_rosu_negru *parent = x->getParent(), *grandparent = parent->getParent(), *uncle = x->uncle();

        if (parent->getColor() != BLACK)
        {
            if (uncle != NULL && uncle->getColor() == RED)
            {
                // daca unchiul este rosu, se face recolorare
                parent->setColor(BLACK);
                uncle->setColor(BLACK);
                grandparent->setColor(RED);
                fixRedRed(grandparent);
            }
            else
            {
                // daca unchiul este negru, se fac rotatii
                if (parent->isOnLeft())
                {
                    if (x->isOnLeft())
                        swapColors(parent, grandparent);
                    else
                    {
                        leftRotate(parent);
                        swapColors(x, grandparent);
                    }
                    rightRotate(grandparent);
                }
                else
                {
                    if (x->isOnLeft())
                    {
                        rightRotate(parent);
                        swapColors(x, grandparent);
                    }
                    else
                        swapColors(parent, grandparent);
                    leftRotate(grandparent);
                }
            }
        }
    }

    Nod_rosu_negru *successor(Nod_rosu_negru *x)
    {
        Nod_rosu_negru *temp = x;
        while (temp->getLeft() != NULL)
            temp = temp->getLeft();
        return temp;
    }

    Nod_rosu_negru *BSTreplace(Nod_rosu_negru *x)
    {
        if (x->getLeft() != NULL and x->getRight() != NULL)
            return successor(x->getRight());
        if (x->getLeft() == NULL and x->getRight() == NULL)
            return NULL;
        if (x->getLeft() != NULL)
            return x->getLeft();
        else
            return x->getRight();
    }

    void deleteNode(Nod_rosu_negru *v)
    {
        Nod_rosu_negru *u = BSTreplace(v);

        bool uvBlack = ((u == NULL or u->getColor() == BLACK) and (v->getColor() == BLACK));
        Nod_rosu_negru *parent = v->getParent();

        if (u == NULL)
        {
            if (v == root)
            root = NULL;
            else
            {
                if (uvBlack)
                    fixDoubleBlack(v);
                else if (v->sibling() != NULL)
                    v->sibling()->setColor(RED);
                if (v->isOnLeft())
                    parent->setLeft(NULL);
                else
                    parent->setRight(NULL);
            }
            delete v;
            return;
        }

        if (v->getLeft() == NULL or v->getRight() == NULL)
        {
            if (v == root)
            {
                v->setVal(u->getVal());
                v->setLeft(NULL);
                v->setRight(NULL);
                delete u;
            }
            else
            {
                if (v->isOnLeft())
                    parent->setLeft(u);
                else
                    parent->setRight(u);
                delete v;
                u->setParent(parent);
                if (uvBlack)
                    fixDoubleBlack(u);
                else
                    u->setColor(BLACK);
            }
            return;
        }

        swapValues(u, v);
        deleteNode(u);
    }

    void fixDoubleBlack(Nod_rosu_negru *x)
    {
        if (x == root)
            return;

        Nod_rosu_negru *sibling = x->sibling(), *parent = x->getParent();
        if (sibling == NULL)
            fixDoubleBlack(parent);
        else
        {
            if (sibling->getColor() == RED)
            {
                parent->setColor(RED);
                sibling->setColor(BLACK);
                if (sibling->isOnLeft())
                    rightRotate(parent);
                else
                    leftRotate(parent);
                fixDoubleBlack(x);
            }
            else
            {
                if (sibling->hasRedChild())
                {
                    if (sibling->getLeft() != NULL and sibling->getLeft()->getColor() == RED)
                    {
                        if (sibling->isOnLeft())
                        {
                            sibling->getLeft()->setColor(sibling->getColor());
                            sibling->setColor(parent->getColor());
                            rightRotate(parent);
                        }
                        else
                        {
                            sibling->getLeft()->setColor(parent->getColor());
                            rightRotate(sibling);
                            leftRotate(parent);
                        }
                    }
                    else
                    {
                        if (sibling->isOnLeft())
                        {
                            sibling->getRight()->setColor(parent->getColor());
                            leftRotate(sibling);
                            rightRotate(parent);
                        }
                        else
                        {
                            sibling->getRight()->setColor(sibling->getColor());
                            sibling->setColor(parent->getColor());
                            leftRotate(parent);
                        }
                    }
                    parent->setColor(BLACK);
                }
                else
                {
                sibling->setColor(RED);
                if (parent->getColor() == BLACK)
                    fixDoubleBlack(parent);
                else
                    parent->setColor(BLACK);
                }
            }
        }
    }

    void InorderRBT(ostream &out, Nod_rosu_negru *curr)
    {
        if(curr)
        {
            InorderRBT(out, curr->getLeft());
            out << curr->getVal() << " ";
            InorderRBT(out, curr->getRight());
        }
    }

    void OrderRBT(ostream &out, Nod_rosu_negru *x)
    {
        if (x == NULL)
            return;
        queue<pair <Nod_rosu_negru*, int>> q;
        Nod_rosu_negru *curr;
        int inaltimeCurenta = 0;
        q.push({x, inaltimeCurenta});
        out << '\n';
        while (!q.empty())
        {
            curr = q.front().first;
            inaltimeCurenta=q.front().second;
            q.pop();

            out << curr->getVal() << " pe nivelul " << inaltimeCurenta << " culoarea: ";

            if (curr->getColor() == 0)
                cout << "rosu." << '\n';
            else
                cout << "negru." << '\n';

            if (curr->getLeft() != NULL)
                q.push({curr->getLeft(), inaltimeCurenta+1});
            if (curr->getRight() != NULL)
                q.push({curr->getRight(), inaltimeCurenta+1});
        }
    }

    void inaltimea_neagra (Nod_rosu_negru *t, int &nr)
    {
        if (t == NULL)
            return;
        if (t->getColor() == BLACK)
            nr++;
        inaltimea_neagra(t->getLeft(), nr);
    }

    Nod_rosu_negru* makeEmpty(Nod_rosu_negru* t)
    {
        if(t == NULL)
            return NULL;
        {
            makeEmpty(t->getLeft());
            makeEmpty(t->getRight());
            delete t;
        }
        return NULL;
    }

public:

    Arbore_bicolor() { root = NULL; }
    Nod_rosu_negru *getRoot() { return root; }

    ~Arbore_bicolor() { makeEmpty(root); }

    friend istream &operator>> (istream &in, Arbore_bicolor &t)
    {
        int n, x;
        in >> n;
        for (int i = 0; i < n; i++)
        {
            in >> x;
            t.insert (x);
        }
    }

    friend ostream & operator<<(ostream &out, Arbore_bicolor &t)
    {
        out << "Parcurgerea in inordine a arborelui este : ";
        t.InorderRBT(out, t.root);
        cout << '\n' << '\n';
        out << "Parcurgerea pe nivele a arborelui este : ";
        t.OrderRBT(out, t.root);
        out << endl;

        return out;
    }

    Nod_rosu_negru *search(int n)
    {
        Nod_rosu_negru *temp = root;
        while (temp != NULL)
        {
            if (n < temp->getVal())
            {
                if (temp->getLeft() == NULL)
                    break;
                else
                    temp = temp->getLeft();
            }
            else if (n == temp->getVal())
                break;
            else
            {
                if (temp->getRight() == NULL)
                    break;
                else
                    temp = temp->getRight();
            }
        }

    return temp;
    }

    void insert(int n)
    {
        Nod_rosu_negru *newNode = new Nod_rosu_negru(n);
        if (root == NULL)
        {
            newNode->setColor(BLACK);
            root = newNode;
        }
        else
        {
            Nod_rosu_negru *temp = search(n);

            if (temp->getVal() == n)
                return;
            newNode->setParent(temp);

            if (n < temp->getVal())
                temp->setLeft(newNode);
            else
                temp->setRight(newNode);

            fixRedRed(newNode);
        }
    }

    void deleteByVal(int n)
    {
        if (root == NULL)
            return;

        Nod_rosu_negru *v = search(n), *u;

        if (v->getVal() != n)
        {
            cout << "No node found to delete with value:" << n << endl;
            return;
        }

        deleteNode(v);
    }

    int get_depth()
    {
        int nr = 0;
        inaltimea_neagra(getRoot(), nr);
        return nr;
    }

};

int main()
{
    cout << "-----       ARBORE ROSU-NEGRU       -----"<< '\n' << '\n';
    Arbore_bicolor ARN;
    ifstream fin ("date.in");

    fin >> ARN;

    cout << ARN;

    cout << "Se sterge 18" << '\n';

    ARN.deleteByVal(18);
    cout << '\n';

    cout << ARN;

    cout << "Inaltimea neagra a arborelui este: " << ARN.get_depth() << '\n' << '\n';

    cout << "-----       ARBORE binar de cautare       -----"<< '\n' << '\n';

    ABC x;

    fin >> x;

    cout << x;

    x.remove(3);

    cout << x;

    cout << "Inaltimea arborelui binar de cautare este: " << x.get_depth() << '\n';



    return 0;
}
