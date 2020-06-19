#include <iostream>
using namespace std;

struct coada{
    int info;
    coada *urm;
}*prim, *ultim;

void push (int a, coada *&prim){
    coada *p;
    p=new coada;
    p->info=a;
    p->urm=NULL;
    if (prim==NULL){
        prim=ultim=p;
    }
    else{
        ultim->urm=p;
        ultim=p;
    }
}

void afisare (coada *prim){
    coada *p=prim;
    while (p!=NULL){
        cout<<p->info<<" ";
        p=p->urm;
    }
    cout<<endl;
}

int pop (coada *&prim){
    coada *p;
    int k=prim->info;
    p=prim;
    prim=prim->urm;
    delete p;
    return k;
}

int peek (coada *prim){
    return prim->info;
}

bool empty (coada *prim){
    if (prim==NULL)
        return 1;
    return 0;
}

int search (int a, coada *prim){
    coada *p=prim;
    int nr=0,a=-1;
    while (p!=NULL){
        if (p->info==a)
            return nr;
        p=p->urm;
    }
    return a;
}

int main()
{
    int x,n;
    cin>>n;
    for (int i=0;i<n;i++){
        cin>>x;
        push(x,prim);
    }
    pop(prim);
    afisare(prim);

    return 0;
}
