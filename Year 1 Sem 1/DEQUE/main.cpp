#include <iostream>
using namespace std;

struct coada{
    int info;
    coada *urm;
}*prim, *ultim;

void push_final (int a, coada *&prim, coada *&ultim){
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

void push_inceput (int a, coada *&prim){
    coada *p=new coada;
    p->urm=prim;
    prim=p;
    prim->info=a;
}

void afisare (coada *prim){
    coada *p=prim;
    while (p!=NULL){
        cout<<p->info<<" ";
        p=p->urm;
    }
    cout<<endl;
}

int pop_inceput (coada *&prim){
    coada *p;
    int k=prim->info;
    p=prim;
    prim=prim->urm;
    delete p;
    return k;
}

int pop_final(coada *prim, coada *&ultim){
    coada *penultim=prim;
    while (penultim->urm->urm!=NULL)
        penultim=penultim->urm;
    penultim->urm=NULL;
    delete ultim;
    ultim=penultim;
}

int main()
{
    int x,n;
    cin>>n;
    for (int i=0;i<n;i++){
        cin>>x;
        push_final(x,prim,ultim);
    }
    pop_final(prim,ultim);
    afisare(prim);

    return 0;
}
