#include <iostream>
using namespace std;

struct stiva{
    int info;
    stiva *trec;
}*varf=0;

void push (int x, stiva *&varf){
    stiva *s=varf,*p=varf;
    p=new stiva;
    p->info=x;
    if (p==0){
        p->trec=0;
        varf=p;
    }
    else{
        p->trec=s;
        varf=p;
    }
    s=p;
}

int pop (stiva *&varf){
    stiva *p=varf;
    varf=varf->trec;
    return p->info;
}

int peek (stiva *varf){
    return varf->info;
}

bool emty (stiva *varf){
    if (varf==0)
        return 0;
    return 1;
}

int search (int a, stiva *varf){
    stiva *p=varf;
    int k=0;
    while (p!=0){
        if (p->info==a)
            return k;
        p=p->trec;
        k++;
    }
    return -1;
}

void afisare (){
    stiva *p=varf;
    while (p!=0){
        cout<<p->info<<" ";
        p=p->trec;
    }
}

int main()
{
    int n,x,k;
    cin>>n;
    for (int i=1;i<=n;i++){
        cin>>x;
        push(x, varf);
    }
    cout<<emty(varf);
    afisare();


    return 0;
}
