#include <iostream>
using namespace std;

struct nod{
    int info;
    nod *urm;
};
nod *prim,*ultim;

void adaugare_final(){
    nod *p;
    p=new nod;
    cin>>p->info;
    p->urm=NULL;
    if (prim==NULL){
        prim=ultim=p;
    }
    else{
        ultim->urm=p;
        ultim=p;
    }
}

void add_inceput(){
    nod *p=new nod;
    cin>>p->info;
    p->urm=prim;
    prim=p;
}

void sterg_inceput(){
    nod *aux;
    aux=prim;
    prim=prim->urm;
    delete aux;
}

void sterg_final (){
    nod *penultim=prim;
    while (penultim->urm->urm!=NULL)
        penultim=penultim->urm;
    penultim->urm=NULL;
    delete ultim;
    ultim=penultim;
}

void afisare (){
    nod *p;
    p=prim;
    while (p!=NULL){
        cout<<p->info<<" ";
        p=p->urm;
    }
    cout<<endl;
}

void adaug_dupa_val (int val, int x){
    nod *p,*q;
    p=prim;
    while (p!=NULL){
        if (p->info==val){
            q=new nod;
            q->urm=p->urm;
            p->urm=q;
            q->info=x;
            return;
        }
        p=p->urm;
    }
        cout<<"Nu exista "<<val<<endl;


}

void sterg_dupa_val (int val){
    nod *p,*q;
    p=prim;
    if (p->info==val){
        prim=p->urm;
        delete p;
        return;
    }
    while (p!=NULL){
        if (p->urm->info==val){
            p->urm=p->urm->urm;
            delete p->urm;
            return;
        }
        p=p->urm;
    }
    cout<<"Nu exista "<<val<<endl;
}

void stergere_lista(){
    nod *q;
    while (prim!=NULL){
        q=prim->urm;
        delete prim;
        prim=q;
    }
}

void numarare (int &nr, float &ma){
    nod *p=prim;
    int nri=0,s=0;
    nr=0;
    while (p!=NULL){
        if (p->info%2==0)
            nr++;
    p=p->urm;
    }
    p=prim;
    while (p!=NULL){
        if (p->info%2==1){
            nri++;
            s=s+p->info;
        }
        p=p->urm;
    }
    ma=s/nri;
}

void media (){
    nod *p=prim,*q;
    while (p!=ultim){
        q=new nod;
        q->info=0;
        q->urm=p->urm;
        p->urm=q;
        p=p->urm->urm;
    }
    p=prim;
    while (p!=ultim){
        if (p->urm->info==0)
            p->urm->info=(p->info+p->urm->urm->info)/2;
        p=p->urm;
    }
}

void nr_mari (){
    long a,b,s;
    nod *p=prim;
    cin>>a>>b;
    s=a+b;
    while (s){
        p=new nod;
        p->info=s%10;
        s=s/10;
        p->urm=NULL;
        if (prim==NULL){
            prim=ultim=p;
        }
        else{
            ultim->urm=p;
            ultim=p;
        }
    }
}

int main()
{
    int n,i,nr;
    float ma;
    nr_mari();
    afisare();



    return 0;
}
