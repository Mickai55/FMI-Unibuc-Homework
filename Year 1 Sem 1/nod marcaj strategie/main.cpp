#include <iostream>
using namespace std;

struct nod{
    int info;
    nod *next,*prev;
}*prim,*ultim,*Start,*k;

void adaugare_final(nod *&prim , nod *&ultim , int x){
    nod *p;
    p=new nod;
    p->info=x;
    p->next=NULL;
    p->prev=ultim;
}

void adaugare(nod *&prim , int x){
    nod *p;
    p=new nod;
    if (Start==NULL){
        Start=p;
    }
    else if (prim==NULL){
        prim=ultim=p;
        prim->prev=Start;
        Start->next=prim;
    }
    else{
        ultim->next=Start;
        ultim=p;
    }
    p->info=x;
    p->prev=Start;
    Start->next=p;
    p->next=prim;
    prim->next->prev=p;
    prim=p;
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
    nod *p=Start;
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
    adaugare_inceput(prim,100);
    afisare(prim);



    return 0;
}
