#include <iostream>
using namespace std;

struct nod{
    int info,prio;
    nod *next;
}*prim,*ultim;

void adaugare_final(nod *&prim , nod *&ultim , int x , int y){
    nod *p,*u=prim;
    p=new nod;
    p->info=x;
    p->prio=y;
    p->next=NULL;
    if (prim==NULL){
        prim=ultim=p;
    }
    else{
        ultim->next=p;
        ultim=p;
    }
}

void adaugare_inceput(nod *&prim , int x, int y){
    nod *p;
    p=new nod;
    p->info=x;
    p->prio=y;
    p->next=prim;
    prim=p;
}

void adaugare_i (nod *prim , int k , int x, int z){
    nod *p,*y=prim,*u;
    int i=0;
    p=new nod;
    p->info=x;
    p->prio=z;
    while (y!=NULL){
        if (i==k){
            p->next=y;
            u->next=p;
            return;
        }
        i++;
        u=y;
        y=y->next;
    }
}

void adaugare (nod *&prim, nod *&ultim, int x, int y){
    nod *p=prim;
    int a=0;
    if (prim==NULL)
        adaugare_final(prim,ultim,x,y);
    else if (y>=prim->prio)
        adaugare_inceput(prim,x,y);
    else if (y<ultim->prio)
        adaugare_final(prim,ultim,x,y);
    else{
        while (p->prio>y){
            p=p->next;
            a++;
        }
        adaugare_i(prim,a,x,y);
    }
}

void afisare (nod *prim){
    nod *p=prim;
    while (p!=NULL){
        cout<<p->info<<" "<<p->prio;
        p=p->next;
        cout<<endl;
    }
    cout<<endl;
}

int main()
{
    int n,x,y;
    cin>>n;
    for (int i=0;i<n;i++){
        cin>>x>>y;
        adaugare(prim,ultim,x,y);
    }
    afisare(prim);


    return 0;
}
