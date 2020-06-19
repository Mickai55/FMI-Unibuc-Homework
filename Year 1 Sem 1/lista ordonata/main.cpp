#include <iostream>
using namespace std;

struct nod{
    int info;
    nod *urm;
};
nod *prim,*ultim;

void adaugare_final(int x){
    nod *p;
    p=new nod;
    p->info=x;
    p->urm=NULL;
    if (prim==NULL){
        prim=ultim=p;
    }
    else{
        ultim->urm=p;
        ultim=p;
    }
}

void adaugare_inceput(int x){
    nod *p=new nod;
    p->info=x;
    p->urm=prim;
    prim=p;
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

int main()
{
    int n,i,nr,k;
    nod *q,*y,*u=prim;
    cin>>n;
    cin>>k;
    adaugare_final(k);
    for (i=2;i<=n;i++){
        cin>>k;
        if (k<prim->info)
            adaugare_inceput(k);
        else if (k>ultim->info)
            adaugare_final(k);
        else{
            u=prim;
            while (k>u->info){
                y=u;
                u=u->urm;
            }
            q=new nod;
            q->urm=y->urm;
            y->urm=q;
            q->info=k;
        }
    }
    afisare();


    return 0;
}
