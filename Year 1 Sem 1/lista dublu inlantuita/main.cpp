#include <iostream>
using namespace std;

struct nod{
    int info;
    nod *next,*prev;
}*prim,*ultim;

void adaugare_final(nod *&prim , nod *&ultim , int x){
    nod *p,*u;
    p=new nod;
    p->info=x;
    p->next=NULL;
    p->prev=ultim;
    if (prim==NULL){
        prim=ultim=p;
    }
    else{
        ultim->next=p;
        ultim=p;
    }
    u=p;
}

void adaugare_inceput(nod *&prim , int x){
    nod *p;
    p=new nod;
    p->info=x;
    p->prev=NULL;
    p->next=prim;
    prim=p;
}

void adaugare_i (nod *prim , int k , int x){
    nod *p,*y=prim;
    int i=0;
    p=new nod;
    p->info=x;
    while (y!=NULL){
        if (i==k){
            p->prev=y->prev;
            y->prev->next=p;
            p->next=y;
            y->prev=p;
            return;
        }
        i++;
        y=y->next;
    }
}

void stergere_i (nod *&prim , nod *&ultim , int n , int k){
    nod *p=prim,*y;
    int i=0;
    if (k==0){
        y=prim;
        prim=prim->next;
        prim->prev=NULL;
        delete y;
        return;
    }
    if (k==n){
        y=ultim;
        ultim=ultim->prev;
        ultim->next=NULL;
        delete y;
        return;
    }
    while (p!=NULL){
        if (i==k){
            y=p;
            p=p->prev;
            p->next=y->next;
            y->next->prev=p;
            delete y;
            return;
        }
        p=p->next;
        i++;
    }
}

void stergere_val (nod *&prim , nod *&ultim , int n , int k){
    nod *p=prim,*y;
    int i=0;
    if (i==0&&k==p->info){
        y=prim;
        prim=prim->next;
        prim->prev=NULL;
        delete y;
        return;
    }
    if (i==n&&k==p->info){
        y=ultim;
        ultim=ultim->prev;
        ultim->next=NULL;
        delete y;
        return;
    }
    while (p!=NULL){
        if (k==p->info){
            y=p;
            p=p->prev;
            p->next=y->next;
            y->next->prev=p;
            delete y;
            return;
        }
        p=p->next;
        i++;
    }
}

void afisare (nod *prim){
    nod *p=prim;
    while (p!=NULL){
        cout<<p->info<<" ";
        p=p->next;
    }
    cout<<endl;
}

void afisare_inversa (nod *ultim){
    nod *p=ultim;
    while (p!=NULL){
        cout<<p->info<<" ";
        p=p->prev;
    }
    cout<<endl;
}

int main()
{
    int n,x;
    cin>>n;
    for (int i=0;i<n;i++){
        cin>>x;
        adaugare_final(prim,ultim,x);
    }
    stergere_val(prim,ultim,n,3);
    afisare_inversa(ultim);


    return 0;
}
