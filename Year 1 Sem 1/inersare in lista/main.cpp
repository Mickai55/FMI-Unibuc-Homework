#include <iostream>
using namespace std;

struct nod{
    int info;
    nod *urm;
};
nod *primA,*ultimA,*primB,*ultimB;

void afisare (nod *prim){
    nod *p;
    p=prim;
    while (p!=NULL){
        cout<<p->info<<" ";
        p=p->urm;
    }
    cout<<endl;
}

void add_inceput(nod *&prim, int x){
    nod *p=new nod;
    p->info=x;
    p->urm=prim;
    prim=p;
}

void adaugare_final(nod *&prim, nod *&ultim){
    nod *p;
    p=new nod;
    cin>>p->info;
    add_inceput(primB,p->info);
    p->urm=NULL;
    if (prim==NULL){
        prim=ultim=p;
    }
    else{
        ultim->urm=p;
        ultim=p;
    }
}

int main()
{
    int n,i,nr;
    cin>>n;
    for (i=1;i<=n;i++)
        adaugare_final(primA,ultimA);
    afisare(primB);




    return 0;
}
