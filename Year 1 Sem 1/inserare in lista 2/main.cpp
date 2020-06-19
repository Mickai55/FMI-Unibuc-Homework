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

void afisare (){
    nod *p;
    p=prim;
    while (p!=NULL){
        cout<<p->info<<" ";
        p=p->urm;
    }
    cout<<endl;
}

int main()
{
    int n,i,nr;
    float ma;
    nr_mari();
    afisare();



    return 0;
}
