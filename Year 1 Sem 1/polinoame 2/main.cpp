#include <iostream>
#include <math.h>
using namespace std;
struct pol{
    int gr,coef;
    pol *urm;
};
pol *primP,*ultimP,*primQ,*ultimQ;
int n,m,x[100];
void creare (int k, pol *&prim, pol *&ultim){
    int i;
    pol *p;
    for (i=k;i>=0;i--){
        p=new pol;
        p->gr=i;
        cin>>p->coef;
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

void afisare (pol *prim){
    pol *p;
    p=prim;
    while (p!=NULL){
        cout<<p->coef<<"*x^"<<p->gr<<" ";
        p=p->urm;
    }
    cout<<endl;
}

void inmultire (pol *prim,int a,int x){
    int i;
    pol *p=prim;
    for (i=a;i>=1;i--){
        p->coef=p->coef*x;
        p=p->urm;
    }

}

int punct (pol *prim,int a,int x){
    int i,s=0;
    pol *p=prim;
    for (i=a;i>=0;i--){
        s=s+p->coef*pow(x,i);
        p=p->urm;
    }
    return s;
}

void suma (){
    int i;
    pol *p=primP,*q=primQ;
    cout<<"P+Q=";
    if (n>m){
        for (i=n;i>=0;i--){
            if (q->gr==i){
                cout<<p->coef+q->coef<<"*x^"<<i<<" ";
                q=q->urm;
            }
            else
                cout<<p->coef<<"*x^"<<i<<" ";
            p=p->urm;
        }

    }
    else{
        for (i=m;i>=0;i--){
            if (p->gr==i){
                cout<<p->coef+q->coef<<"*x^"<<i<<" ";
                p=p->urm;
            }
            else
                cout<<q->coef<<"*x^"<<i<<" ";
            q=q->urm;
        }

    }

}

void produsPQ (){
    int i,j;
    pol *p=primP,*q=primQ;
    cout<<"P*Q=";
    for (i=n;i>=0;i--){
        q=primQ;
    for (j=m;j>=0;j--){
        x[i+j]=x[i+j]+p->coef*q->coef;
        q=q->urm;
    }
        p=p->urm;
    }
    for (i=m+n;i>=0;i--)
        cout<<x[i]<<"*x^"<<i<<" ";

}

int main()
{
    cout<<"n=";cin>>n;
    creare (n,primP,ultimP);
    cout<<"m=";cin>>m;
    creare (m,primQ,ultimQ);
    afisare(primP);
    afisare(primQ);
    produsPQ();


    return 0;
}
